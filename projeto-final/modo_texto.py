#coding: utf-8


from tabelas import *
configura_banco_de_dados()


def menu():

    print("""
    |-------------------------------|
    |    Sistema de Vendas          | 
    |-------------------------------|
    |           MENU                |
    |-------------------------------|
    | 1 - Cadastrar produtos        |
    | 2 - Apagar produtos           |
    | 3 - Listar produtos           |
    | 4 - Alterar preço de produto  |
    | ----------------------------- |
    | 5 - Cadastrar clientes        |
    | 6 - Apagar clientes           |
    | 7 - Alterar nome de cliente   |
    | 8 - Listar clientes           |
    | ----------------------------- |
    | 9 - Cadastrar vendas          |
    | 10 - Apagar vendas            |
    | 11 - Listar vendas            |
    | 12 - Inserir produto em venda |
    | ----------------------------- |
    | 13 - sair                     |
    |-------------------------------|
    """)
    opcao = input("Informe o número da opção desejada: ")
    print("\n")
    return int(opcao)


def produtos_cadastrar():
    print("Cadastrar produto")
            
    nome_digitado = input("> informe o nome: ")
    preco_digitado = input("> informe o preço: ")

    produto_id = Produtos.insert(nome=nome_digitado, preco=preco_digitado).execute()
    print(" Produto foi cadastrado com sucesso e possui id = %d " % produto_id)
    input()

def produtos_listar():
    print("Produtos")
    print("| id | nome                 | preco |")

    lista_de_produtos = Produtos.select()
    for produto in lista_de_produtos:
        print("| %2d | %-20s | %5s |" %(produto.id, produto.nome, produto.preco))

def produtos_apagar():
    print("Apagar produtos")
    produtos_listar()
    id_produto = input("> Informe o id do produto que deseja apagar: ")

    deletou = Produtos.delete().where(Produtos.id == id_produto).execute()
    if deletou:
        print(" Produto deletado! ")
    else:
        print(" Error: não existe produto com esse id! ")
    input()

# loop principal
opcao = 0
while opcao != 14: 

    opcao = menu()

    if opcao == 1:
        produtos_cadastrar()
    if opcao == 2:
        produtos_listar()
    if opcao == 3:
        produtos_apagar()


# vim: set ts=4 sw=4 sts=4 expandtab:
