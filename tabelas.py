from peewee import PostgresqlDatabase, Model

pg_db = PostgresqlDatabase('meu_banco_de_dados', user='postgres', password='secret',
                           host='127.0.0.1', port=5432)
                           
class BaseModel(Model):
    """Um modelo que serve de base para o banco de dados postgre."""
    class Meta:
        database = pg_db
        
class Usuario(BaseModel)
    nome = Charfield()
    senha = Charfield(null=true)
    foto_url = CharField(null=true)
    email = CharField(null=true)
    
