import MySQLdb

class FabricaConexao():
    @staticmethod
    def conectar():
        db = MySQLdb.connect(
            user="cafe",
            passwd="SenhaForte123!",
            db="treinaweb_clientes",
            host="localhost",
            port=3306,
            autocommit=True
        )
        return db
