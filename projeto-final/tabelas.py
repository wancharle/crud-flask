#coding: utf-8
from peewee import * 

# informa o arquivo onde o banco de dados será guardado
banco_de_dados = SqliteDatabase("banco_de_dados.db")

class ModeloBase(Model):
    """Um modelo que serve de base para as outras classes herdarem"""
    class Meta:
        database = banco_de_dados 

# classe que representa a tabela Produtos
class Produtos(ModeloBase):
    id = IntegerField(primary_key=True)
    nome = CharField()
    preco = CharField()


# classe que representa a tabela Clientes 
class Clientes(ModeloBase):
    id = IntegerField(primary_key=True)
    nome = CharField()


# classe que representa a tabela Vendas 
class Vendas(ModeloBase):
    id = IntegerField(primary_key=True)
    cliente_id = ForeignKeyField(Clientes, column_name="cliente_id", backref="vendas")
    data = CharField()

# classe que representa a tabela Vendas 
class Produtos_venda(ModeloBase):
    id = IntegerField(primary_key=True)
    venda_id = ForeignKeyField(Vendas, column_name="venda_id", backref="produtos_venda")
    produto_id = ForeignKeyField(Produtos, column_name="produto_id", backref="produtos_venda")
    quantidade = IntegerField(default=1)
    valor = DoubleField()


def configura_banco_de_dados():
    # conecta no banco de dados
    banco_de_dados.connect()
    # cria as talelas (Produtos, Vendas, Clientes e ProdutosVenda) no banco de dados se ainda não existirem.
    banco_de_dados.create_tables([ Produtos, Clientes, Vendas ])
