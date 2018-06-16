#coding: utf-8

from peewee import *

banco_de_dados = SqliteDatabase("c:/projetos/banco_de_dados.db")

class ModeloBase(Model):
	class Meta:
		database = banco_de_dados
		
		
class Pessoa(ModeloBase):
	nome = CharField()
	telefone = CharField()
	
	
def configura_banco():
	banco_de_dados.connect()
	banco_de_dados.create_tables([Pessoa])