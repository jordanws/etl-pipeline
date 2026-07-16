import sqlite3

conexaoBd = sqlite3.connect('banco.db')

cursor = conexaoBd.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id_cliente INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome    TEXT NOT NULL
    );
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedidos (
        id_pedido INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER NOT NULL,
        produto TEXT NOT NULL,
        preco REAL,
        FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
    );
""")

conexaoBd.commit()
conexaoBd.close()

print("Tabela Gerada")