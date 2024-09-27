import os

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho():
    print("\n*********************************************")
    print("********* Bem vindo ao sistema CTRL *********")
    print("*********************************************")

def encerramento():
    limpar_console()
    print("\n**********************************************")
    print("**** Obrigado por utilizar o sistema CTRL ****")
    print("**********************************************\n")

produtos = []


def cadastro():

    limpar_console()
    produto = ""
    while produto == "" :
        produto = input("Qual o nome do produto? ")
        if produto == "":
            print("Nome inválido, tente novamente")
        else:
            produtos.append(produto)

    valor = ""
    while valor == "":
        valor = float(input("Qual o valor do produto? "))
        if valor == "":
            print("Valor inválido, tente novamente.")
        else:
            produtos.append(valor)

    qtd = int(input("Qual a quantidade? "))
    produtos.append(f"{qtd}x")
    
def deletar():
    limpar_console()
    for i in range(0, len(produtos),3):
        lista_rec = produtos[i:i+3]
        print(' | '.join(map(str,lista_rec)))

    produto_del = input("\nQual produto você deseja deletar? ")
    for i in range(0, len(produtos)):
        if produtos[i] == produto_del:
            del produtos[i]
            del produtos[i]
            del produtos[i]
            print(f"\n{produto_del}, foi deletado.")
            break
        limpar_console()
        
def vizualizar():
    limpar_console()
    for i in range(0, len(produtos),3):
        lista_rec = produtos[i:i+3]
        print(' | '.join(map(str,lista_rec)))
            
def somaTotal():
    soma = 0
    limpar_console()
    for i in range(1, len(produtos)-1, 3):
        soma += produtos[i]
    print(soma)
    
