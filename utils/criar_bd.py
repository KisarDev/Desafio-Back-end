import sqlite3

def criar_banco_de_dados(db_file):
            connection = sqlite3.connect(db_file)
            cursor = connection.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY,
                nome TEXT
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS ordens_producao (
                id INTEGER PRIMARY KEY,
                quantidade INTEGER,
                data_entrega TEXT,
                status TEXT,
                data_conclusao TEXT
            )
            """)
            connection.commit()
            connection.close()