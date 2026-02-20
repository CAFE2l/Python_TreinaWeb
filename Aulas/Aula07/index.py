import MySQLdb, cliente, cliente_repositorio, fabrica_conexao


cliente = cliente.Cliente("FINALMENTEEEEEE", 777)

cliente_repositorio.ClienteRepositorio.listar_clientes()
cliente_repositorio.ClienteRepositorio.inserir_cliente(cliente)
#cliente_repositorio.ClienteRepositorio.editar_cliente(3, cliente)
#cliente_repositorio.ClienteRepositorio.remove_cliente(6)

