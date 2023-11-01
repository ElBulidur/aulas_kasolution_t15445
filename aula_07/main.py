from manage import Manager

def start():
    trabalho = Manager()
    usuarios = [
        ('Julio', 'biscoito'),
        ('Andre', '234hnd'),
        ('Marcello', 'jsaodsda'),
        ('Fabio', 'jhsadnlsa')
    ]

    # trabalho.pegar_conexao() # ativar conexao

    # trabalho.criar_usuario('Andre', 'Bolaquadrada') # criar usuario

    # trabalho.atualizar_usuario('Pereira', 'bolinhadegude', 2) # atualizar usuario

    # trabalho.deletar_usuario(3) # deletar usuario


    for usuario, senha in usuarios:
        pass
        # trabalho.pegar_conexao() 
        # trabalho.criar_usuario(usuario, senha)
        

    trabalho.pegar_usuario_por_id(5)
    
    trabalho.pegar_todos_usuarios()
    
if __name__ == '__main__':
    start()