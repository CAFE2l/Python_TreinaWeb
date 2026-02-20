
import MySQLdb, configparser

class FabricaConexao():
    @staticmethod
    def conectar():
        config = configparser.ConfigParser()
        config.read('Aulas/Aula07/config.ini')  # caminho ajustado

        db = MySQLdb.connect(
            user=config['DATABASE']['user'],
            passwd=config['DATABASE']['passwd'],
            db=config['DATABASE']['db'],   # corrigido
            host=config['DATABASE']['host'],
            port=int(config['DATABASE']['port']),
            autocommit=config['DATABASE'].getboolean('autocommit')
        )
        return db
