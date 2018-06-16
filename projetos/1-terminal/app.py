#coding: utf-8

from tabelas import *
configura_banco()

print("Bem vindo!\n\n")
print("|---- Cadastro de Pessoa -----|")

nome = raw_input("Informe o nome: ") 
telefone =  raw_input("Informe o Telefone: ")

# salvar dados no banco de dados
nova_pessoa = Pessoa()
nova_pessoa.nome = nome
nova_pessoa.telefone = telefone
nova_pessoa.save() # salva os dados no banco de dados
# fim

print("\nA pessoa `%s` foi registrada no nosso sistema con o telefone `%s`!" % (nome, telefone))
raw_input()
