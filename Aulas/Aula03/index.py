import MySQLdb

db = MySQLdb.connect(
    user="cafe",
    passwd="SenhaForte123!",
    db="treinaweb_clientes",
    host="localhost",
    port=3306,
    autocommit=False
)
cursor = db.cursor()
cursor.execute("SELECT * FROM clientes")
print(cursor.fetchall())
print("conexaao realizda com sucesso")
try:
    db.begin()
    cursor.execute("INSERT INTO clientes (nome, idade) VALUES ('luis gustavo', 16)")
    cursor.execute("INSERT INTO clientes (nome, idade) VALUES ('cavalo', 122)")
    db.commit()
except: 
    db.rollback()
cursor.execute("SELECT * FROM clientes")
#print(cursor.lastrowid)
#cursor.execute("UPDATE clientes SET nome='Ana' WHERE idcliente=1")
#cursor.execute("DELETE FROM clientes WHERE nome='luis gustavo'")
#cursor.execute("SELECT * FROM clientes")
#print(cursor.fetchall())


db.close()

