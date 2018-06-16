#coding: UTF-8

from tabelas import *
configura_banco()

from flask import Flask, render_template, request

app =  Flask(__name__)

@app.route("/")
def pagina_index():
	return render_template("index.html")
	
@app.route("/cadastrar/", methods=["GET","POST"])
def cadastrar():
	nome = request.form.get("nome")
	telefone = request.form.get("telefone")
	
	# salvar dados no banco de dados
	nova_pessoa = Pessoa()
	nova_pessoa.nome = nome
	nova_pessoa.telefone = telefone
	nova_pessoa.save() # salva os dados no banco de dados
	# fim
	
	return render_template("cadastro_realizado.html",**locals())

	