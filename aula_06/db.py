import mysql.connector


try:
    conn_mysql = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='db_funcionarios'
    )
    # CRUD = CREATE, READ, UPDATE e DELETE
    print("Conexao realizada com sucesso!")
    
    
    sql = 'INSERT INTO tbfuncionarios(Nome, Idade, Cargo, Salario, IRPF) Values (%s, %s, %s, %s, %s)'

    cursor = conn_mysql.cursor()

    cursor.execute(sql, ['Julio', 18, 'Professor', 200.00, 20.90])
    conn_mysql.commit()

    conn_mysql.close()
    
    print("Inserido com sucesso!!")
    
    
except Exception as e:
    print(e)




