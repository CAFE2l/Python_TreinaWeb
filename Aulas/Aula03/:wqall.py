import MySQLdb

db = MySQLdb.connect(
    user="cafe",
    passwd="SenhaForte123!",
    db="treinaweb_clientes",
    host="localhost",
    port=3306
)
cursor = db.cursor()
cursor.execute("SELECT * FROM clientes")
print(cursor.fetchall())
print("conexao realizda com sucesso")
cursor.execute("INSERT INTO clientes (nome, idade) VALUES ('luis gustavo', 16)")
cursor.execute("SELECT * FROM clientes")
print(cursor.fetchall())
print(cursor.lastrowid)
cursor.execute("UPDATE clientes SET nome='Ana' WHERE idcliente=1")
cursor.execute("SELECT * FROM clientes")
print(cursor.fetchall())
db.close()

