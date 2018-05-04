from peewee import PostgresqlDatabase, Model, CharField

pg_db = PostgresqlDatabase('teste', user='postgres', password='example',
                           host='192.168.99.100', port=32776)
                           
class BaseModel(Model):
    """Um modelo que serve de base para o banco de dados postgre."""
    class Meta:
        database = pg_db
        
class Usuario(BaseModel):
	nome = CharField()
	senha = CharField(null=True)
	foto_url = CharField(null=True)
	email = CharField(null=True)
