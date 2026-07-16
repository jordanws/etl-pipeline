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

cursor.execute("DELETE FROM pedidos")
cursor.execute("DELETE FROM clientes")

cursor.execute("INSERT INTO clientes (nome) VALUES (?)", ('João Silva',))
cursor.execute("INSERT INTO clientes (nome) VALUES (?)", ('Maria Santos',))

cursor.execute("INSERT INTO pedidos (id_cliente, produto, preco) VALUES (?, ?, ?)", (1, 'Notebook', 4000.00))
cursor.execute("INSERT INTO pedidos (id_cliente, produto, preco) VALUES (?, ?, ?)", (2, 'Mouse sem fio', 120.50))
cursor.execute("INSERT INTO pedidos (id_cliente, produto, preco) VALUES (?, ?, ?)", (1, 'Computador(Desktop)', 5600.00))


conexaoBd.commit()
conexaoBd.close()

print("Tabela Gerada")