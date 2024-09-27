
import bibliotecas as b
import time
res = 0

b.cabecalho()

while res != 4:
    print("\n1 - Cadatrar\n2 - Deletar\n3 - Visualizar\n 3.1 - Resumo\n 3.2 - Total\n4 - Sair")
    res = float(input("\nO que deseja fazer?\n"))
    
    if res == 1:
        b.cadastro()

    elif res == 2:
        b.deletar()

    elif res == 3.1:
      b.vizualizar()        

    elif res == 3.2:    
        b.somaTotal()

    else: 
        print("Encerrando sistema...")
        time.sleep(3)
        b.encerramento()
        time.sleep(3)

        

                      



  

    



