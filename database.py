# database.py

import sqlite3

def conectar():
    return sqlite3.connect(
        "data/assistencia.db",
        check_same_thread=False
    )

def criar_banco():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
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
        problema TEXT,
        FOREIGN KEY(cliente_id) REFERENCES clientes(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ordens_servico(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        equipamento_id INTEGER,
        descricao TEXT,
        status TEXT DEFAULT 'Em Análise',
        valor REAL
    )
    """)

    conn.commit()
    conn.close()