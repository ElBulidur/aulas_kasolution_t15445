import mysql.connector


class Conn:
    def __init__(self):
        self.conn_mysql = None
    
    def pegar_conexao(self):
        try:
            
            self.conn_mysql = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='db_usuarios'
            )
            
            if __name__ == '__main__':
                print("Conexao realizada com sucesso!")
                
        except Exception as e:
            pass
        

if __name__ == '__main__':
    Conn().pegar_conexao()