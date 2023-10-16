import sqlite3
from .Produto import Produto

class Fabrica:
    def __init__(self, db_file):
        self.db_file = db_file

    def registrar_ordem_producao(self, produto_nome, quantidade, data_entrega):
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()

        # Busca o ID do produto pelo nome
        cursor.execute("SELECT id FROM produtos WHERE nome=?", (produto_nome,))
        produto = cursor.fetchone()

        if produto is not None:
            # Insere a ordem de produção
            cursor.execute("INSERT INTO ordens_producao (quantidade, data_entrega, status) VALUES (?, ?, ?)",
                        (produto[0], quantidade, data_entrega, "Em andamento"))
            connection.commit()
            connection.close()
            print("Ordem de produção registrada com sucesso.")
        else:
            print("Produto não encontrado. Verifique o nome do produto.")

    def listar_produtos(self):
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute("SELECT nome FROM produtos")
        produtos = cursor.fetchall()
        connection.close()

        for produto in produtos:
            print(f"Produto: {produto[0]}")

    def registrar_ordem_producao(self, produto, quantidade, data_entrega):
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO ordens_producao (quantidade, data_entrega, status) VALUES (?, ?, ?)",
                       (quantidade, data_entrega, "Em andamento"))
        connection.commit()
        connection.close()
        print("Ordem de produção registrada com sucesso.")

    def listar_ordens_producao(self):
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute("SELECT p.nome, o.quantidade, o.data_entrega, o.status FROM ordens_producao o JOIN produtos p ON o.produto_id = p.id")
        ordens = cursor.fetchall()
        connection.close()

        if ordens:
            for ordem in ordens:
                print(f"Produto: {ordem[0]}, Quantidade: {ordem[1]}, Data de Entrega: {ordem[2]}, Status: {ordem[3]}")
        else:
            print("Nenhuma ordem de produção encontrada.")


    def buscar_produto_por_nome(self, nome):
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute("SELECT id, nome FROM produtos WHERE nome=?", (nome,))
        produto_info = cursor.fetchone()
        connection.close()

        if produto_info:
            id, nome = produto_info[0], produto_info[1]
            return Produto(id, nome)
        else:
            return None
