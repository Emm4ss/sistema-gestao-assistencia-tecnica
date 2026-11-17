import sqlite3

DB_NAME = "assistencia.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def criar_banco():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        email TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS equipamentos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        tipo TEXT,
        marca TEXT,
        modelo TEXT,
        serie TEXT,
        FOREIGN KEY(cliente_id) REFERENCES clientes(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ordens_servico(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente TEXT,
        equipamento TEXT,
        problema TEXT,
        status TEXT,
        data_abertura TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()
