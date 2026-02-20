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

nome = "bananinha"
idade = 40
cursor.execute("UPDATE clientes SET nome=%(nome)s, idade=%(idade)s WHERE idcliente=22", ({'nome': nome,
                                                                                          'idade': idade}))
cursor.execute("SELECT * FROM clientes")
print(cursor.fetchall())

db.close()
