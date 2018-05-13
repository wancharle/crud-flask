
from tabelas import Pessoa, db

lista_de_tabelas = [ Pessoa, ]

db.connect()
db.create_tables(lista_de_tabelas)