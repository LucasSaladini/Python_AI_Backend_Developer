import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

connection = sqlite3.connect(ROOT_PATH / "database.db")
cursor = connection.cursor()
cursor.row_factory = sqlite3.Row

def create_table(connection, cursor)
    cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150));")
    connection.commit()

def insert_record(connection, cursor, nome, email)
    data = (nome, email)
    cursor.execute(f"INSERT INTO clientes (nome, email) VALUES (?, ?);", data)
    connection.commit()

def update_record(connection, cursor, nome, email, id)
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    connection.commit()

def delete_record(connection, cursor, id)
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    connection.commit()

def batch_insert(connection, cursor, data)
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES(?, ?);")
    connection.commit()

def fetch_customer(cursor, id)
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

def list_customers(cursor)
    return cursor.execute("SELECT * FROM clientes")


data = [
    ('Guilherme', 'email@exemplo.com'),
    ('Chappie', 'email@exemplo.com'),
    ('Melaine', 'email@exemplo.com')
]

update_record(connection, cursor, 'Guilherme Carvalho', 'email@example.com', 1)
delete_record(connection, cursor, id)
batch_insert(connection, cursor, data)
customer = fetch_customer(cursor, 1)
print(dict(customer))
customers = list_customers(cursor)
for customer in customers:
    print(dict(customer))