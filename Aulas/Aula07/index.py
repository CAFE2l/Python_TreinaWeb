import MySQLdb, cliente

db = MySQLdb.connect(
    user="cafe",
    passwd="SenhaForte123!",
    db="treinaweb_clientes",
    host="localhost",
    port=3306,
    autocommit=True
)
cursor = db.cursor()


def listar_clientes():
    cursor.execute("SELECT * FROM clientes")
    print(cursor.fetchall())


def inserir_cliente(cliente):
    cursor.execute(
        "INSERT INTO clientes (nome, idade) VALUES (%s, %s)",
        (cliente.nome, cliente.idade)
    )


def editar_cliente(id_cliente, cliente):
    cursor.execute("UPDATE clientes SET nome=%(nome)s, idade=%(idade)s WHERE idcliente=%(id_cliente)s",
                   ({'nome': cliente.nome,
                     'idade': cliente.idade,
                     'id_cliente': id_cliente}))

def remover_cliente(id_cliente):
    cursor.execute("DELETE FROM clientes WHERE idcliente=%s", (id_cliente,))


cliente = cliente.Cliente("sabrino", 29)

listar_clientes()
inserir_cliente(cliente)
editar_cliente(3, cliente)
remover_cliente(6)

db.close()
