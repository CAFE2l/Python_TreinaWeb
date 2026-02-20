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

cursor.executemany("INSERT INTO clientes (nome, idade) VALUES(%s, %s)",
                   (
                        ('jose', 50),
                        ('maria', 51),
                        ('pedro', 41),
                        ('fabio filho', 20)
                       ))


db.close()
