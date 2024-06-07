import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

connection = sqlite3.connect(ROOT_PATH / "database.db")
cursor = connection.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", ("Teste 1", "email@exemplo.com"))
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (2, "Teste 1", "email@exemplo.com"))
    connection.commit()
except Exception as exc:
    print(f"Ops! Um erro ocorreu - {exc}")
    connection.rollback()
    