import sqlite3
from datetime import datetime
import os
from utils import criar_banco_de_dados
from entities import Fabrica   

db_file = "fabrica.db"
if not os.path.exists(db_file):
    criar_banco_de_dados(db_file)

    
def main():
    fabrica = Fabrica(db_file)

    while True:
        print("\nOpções:")
        print("1. Registrar Ordem de Produção")
        print("2. Listar Ordens de Produção")
        print("3. Concluir Ordem de Produção")
        print("4. Listar Produtos")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            produto_nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade desejada: "))
            data_entrega = input("Data de entrega (YYYY-MM-DD): ")
            
            produto = fabrica.buscar_produto_por_nome(produto_nome)
            
            if produto:
                fabrica.registrar_ordem_producao(produto, quantidade, data_entrega)
            else:
                print("Produto não encontrado. Verifique o nome do produto.")
        elif escolha == "2":
            fabrica.listar_ordens_producao()
        elif escolha == "3":
            pass
        elif escolha == "4":
            fabrica.listar_produtos()
        elif escolha == "5":
            break


if __name__ == "__main__":
    main()
