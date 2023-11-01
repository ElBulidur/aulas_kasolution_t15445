from database import Conn

class Manager(Conn):
        
    # CREATE [C]RUD    
    def criar_usuario(self, nome, senha):
        
        self.pegar_conexao()
        #query
        sql = 'INSERT INTO tb_usuarios(usuario, senha) Values (%s, %s)'
        
        # Cursor para operacoes
        cursor = self.conn_mysql.cursor()
        
        # Executando as operacoes
        cursor.execute(sql,[nome, senha])
        
        self.conn_mysql.commit()
        
        self.conn_mysql.close()
        
        print("Usuario inserido com sucesso!")
        
    # UPDATE - CR[U]D
    def atualizar_usuario(self, nome, senha, id):
        
        self.pegar_conexao()
        
        sql = 'UPDATE tb_usuarios SET usuario=%s, senha=%s WHERE id=%s'
        
        cursor = self.conn_mysql.cursor()
        
        cursor.execute(sql, [nome, senha, id])
        
        self.conn_mysql.commit()
        
        print(f'Foram alterados {cursor.rowcount} registro(s).')
        
        self.conn_mysql.close()
        
    # DELETE - CRU[D]
    def deletar_usuario(self, id):
        
        self.pegar_conexao()
        
        sql = 'DELETE FROM tb_usuarios WHERE id=%s'
        
        cursor = self.conn_mysql.cursor()
        
        cursor.execute(sql, [id])
        
        self.conn_mysql.commit()
        
        print(f'Foram alterados {cursor.rowcount} registro(s).')
         
        self.conn_mysql.close() 
    
    # READ - C[R]UD
    def pegar_todos_usuarios(self):
        
        self.pegar_conexao()
        
        sql = 'SELECT usuario, senha FROM tb_usuarios'
        
        cursor = self.conn_mysql.cursor()
        
        cursor.execute(sql)
        
        # for registro in cursor:
        #     print(registro)
        
        for usuario, senha in cursor:
            print(f"Usuario: {usuario}, senha: {senha}")
            
        self.conn_mysql.close()
        
    def pegar_usuario_por_id(self, id):
        
        self.pegar_conexao()
        
        sql = 'SELECT usuario, senha FROM tb_usuarios WHERE id=%s'
        
        cursor = self.conn_mysql.cursor()
        
        cursor.execute(sql, [id])
        
        registro = cursor.fetchone()
        
        if registro:
            print(registro)
        else:
            print("Nao foi encontrado no banco de dados!!!")
        
        self.conn_mysql.close()
          
   