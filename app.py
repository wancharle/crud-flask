#encoding: utf-8
import os
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from playhouse.shortcuts import  model_to_dict
from tabelas import Pessoa

app = Flask(__name__)

def processa_upload(name_do_input):
	if name_do_input not in request.files:
		return ""
	else:
		arquivo_temporario = request.files[name_do_input]
		nome_do_arquivo = secure_filename(arquivo_temporario.filename)
		caminho_do_arquivo = "static/uploads/" + nome_do_arquivo
		arquivo_temporario.save(caminho_do_arquivo)
		url_do_arquivo = "/"+caminho_do_arquivo
		return url_do_arquivo

@app.route("/")
def index():
	pessoas = Pessoa.select().order_by(Pessoa.nome_completo)
	return render_template("index.html", lista_de_pessoas = pessoas)
	
		
@app.route("/remover/<id>/")
def remover(id):
	pessoa = Pessoa.get_by_id(id)
	caminho_foto = pessoa.foto_url[1:] # [:1] remove o primeiro caracter da url, ou seja, remove o "/" inicial
	# deleta foto do sistema de arquivo
	os.unlink(caminho_foto)
	# deleta do banco
	Pessoa.delete().where(Pessoa.id==id).execute()
	return redirect("/")

	
@app.route("/cadastrar/",methods=["GET","POST"])
def cadastrar():
	if request.method=="POST":
		try:
			if request.form['usuario'] == "":
				raise Exception(u"usuario não informado!")	
			if request.form['email'] == "":
				raise Exception(u"email não informado!")
			p = Pessoa()
			p.usuario = request.form['usuario'] 
			p.email = request.form['email']
			p.nome_completo = request.form['nome_completo']
			p.senha = request.form['senha']
			p.biografia = request.form['biografia']
			p.foto_url = processa_upload("foto_url")
			p.save()
			return redirect("/")
		except Exception as error:
			return render_template("cadastrar.html", msg_error = error,	form = request.form.to_dict())
	else:
		return render_template("cadastrar.html", form={})

		
@app.route("/editar/<id>/",methods=["GET","POST"])
def atualizar(id):
	if request.method=="POST":
		try:
			if request.form['usuario'] == "":
				raise Exception(u"usuario não informado!")	
			if request.form['email'] == "":
				raise Exception(u"email não informado!")		
			p = Pessoa.get_by_id(id)
			p.usuario = request.form['usuario'] 
			p.email = request.form['email']
			p.nome_completo = request.form['nome_completo']
			p.senha = request.form['senha']
			p.biografia = request.form['biografia']
			p.foto_url = processa_upload("foto_url")
			p.save()
			return redirect("/")
		except Exception as error:
			return render_template("editar.html", id = id,  msg_error = error, form = request.form.to_dict())
	else:
		p = Pessoa.get(id)
		return render_template("editar.html",id = id, form=model_to_dict(p))