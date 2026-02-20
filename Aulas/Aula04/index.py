import MySQLdb

db = MySQLdb.connect(
    user="cafe",
    passwd="SenhaForte123!",
    db="treinaweb_clientes",
    host="localhost",
    port=3306,
    autocommit=True
)
cursor = db.cursor()
nome = "CAFÉ"
cursor.execute(f"INSERT INTO clientes(nome, idade) VALUES('{nome}', 25)")
cursor.execute("SELECT * FROM clientes")
print(cursor.fetchall())

nome = "carlos"

#SQL injection 
cursor.execute(f"UPDATE clientes SET nome='{nome}', idade=80  WHERE idcliente=1")
cursor.execute("SELECT * FROM clientes")
print(cursor.fetchall())
db.close()
