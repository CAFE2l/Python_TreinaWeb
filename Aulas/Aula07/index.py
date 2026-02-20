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


def listar_clientes(self):
    cursor.execute("SELECT * FROM clientes")
    print(cursor.fetchall())


def inserir_cliente(self, cliente):
    cursor.executemany("INSER INTO clientes (nome, idade) VALUES (%s, %s)", cliente.nome, cliente.idade)
    
def editar_cliente(self, id_cliente, cliente):
    cursor.execute("UPDATE clientes SET nome=%(nome)s, idade=%(idade)s WHERE idcliente=%(id_cliente)s",
                   ({'nome': cliente.nome,
                     'idade': cliente.idade,
                     'id_cliente': id_cliente})

def remover_cliente(self, id_cliente):
    cursor.execute("DELETE FROM cliente WHERE idcliente=%s", (id_cliente, ))

listar_clientes()
inserir_cliente(cliente)

db.close()
