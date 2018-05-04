from tabelas import Usuario, pg_db

lista_de_tabelas = [ Usuario, ]

pg_db.connect()
pg_db.create_tables(lista_de_tabelas)
