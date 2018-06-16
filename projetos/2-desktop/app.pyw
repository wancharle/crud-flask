#coding: utf-8
from Tkinter import *
import tkMessageBox

from tabelas import *
configura_banco()
  
class JanelaCadastro:
   
	def __init__(self, janela):
		self.janela = janela
		# cria linhas para inserir os elementos
		self.linha1 = Frame(janela)
		self.linha1["pady"] = 10
		self.linha1.pack()
		self.linha2 = Frame(janela)
		self.linha2["padx"] = 20
		self.linha2.pack()
		self.linha3 = Frame(janela)
		self.linha3["padx"] = 20
		self.linha3.pack()
		self.linha4 = Frame(janela)
		self.linha4["pady"] = 20
		self.linha4.pack()

		# cria o titulo na primeira linha
		self.titulo = Label(self.linha1, text="Cadastro de Pessoa")
		self.titulo["font"] = ("Arial", "10", "bold")
		self.titulo.pack()

		# cria a legenda e caixa de texto para para o item "nome" na segunda linha
		self.nomeLabel = Label(self.linha2,text="Nome")
		self.nomeLabel["width"] = 10
		self.nomeLabel.pack(side=LEFT)
		self.nome = Entry(self.linha2)
		self.nome["width"] = 30
		self.nome.pack(side=LEFT)

		# cria a legenda e caixa de texto para o item "telefone na terceira linha"
		self.telefoneLabel = Label(self.linha3, text="Telefone")
		self.telefoneLabel["width"] = 10
		self.telefoneLabel.pack(side=LEFT)
		self.telefone = Entry(self.linha3)
		self.telefone["width"] = 30
		self.telefone.pack(side=LEFT)

		# cria botao cadastrar
		self.cadastrar = Button(self.linha4)
		self.cadastrar["text"] = "Cadastrar"
		self.cadastrar["command"] = self.cadastrarPessoa 
		self.cadastrar.pack()

	#Método cadastrar pessoa
	def cadastrarPessoa(self):
		nome = self.nome.get() # obtem o nome digitado na caixa de texto
		telefone = self.telefone.get()  # obtem o telefone digitado na caixa de texto
		
		# salvar dados obtidos no banco de dados
		nova_pessoa = Pessoa()
		nova_pessoa.nome = nome
		nova_pessoa.telefone = telefone
		nova_pessoa.save()
		# fim 
		
		mensagem = "A pessoa '%s' foi registrada no nosso sistema com o telefone '%s'!" % (nome, telefone)
		tkMessageBox.showinfo("Pessoa cadastrada!", mensagem)
		
		self.janela.quit()

  
root = Tk()
JanelaCadastro(root)
root.mainloop()