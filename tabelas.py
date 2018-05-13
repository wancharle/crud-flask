from peewee import Model, CharField

from peewee import SqliteDatabase
db = SqliteDatabase("teste.db")

#from peewee import PostgresqlDatabase
#db = PostgresqlDatabase('teste', user='postgres', password='', host='192.168.99.100', port=5432)

                           
class BaseModel(Model):
    """Um modelo que serve de base para o banco de dados postgre."""
    class Meta:
        database = db
        
class Pessoa(BaseModel):
	usuario = CharField(unique=True)
	email = CharField(unique=True)
	nome_completo = CharField()
	senha = CharField(null=True)
	foto_url = CharField(null=True)
	biografia = CharField(null=True)
	