import os

alunos = ['julio', 'henrique', 'izabella', 'matheus']


arquivo = open('usuarios.txt', 'w') # r => Leitura, w => Escrita

arquivo.write('nomes\n')

    
# [arquivo.write(f'{aluno}\n') for aluno in alunos]

# for aluno in alunos:
#     arquivo.write(f'{aluno}\n')

arquivo.close()


with open('novos.log', 'w') as file:
    file.write("INFO - fiz isso!!!\n")
    file.write('ERROR - deu erro!!!\n')
    file.write('WARNING - atencao!!!\n')
    file.write('SUCCESS - sucesso!!!\n')
    
with open('novos.log', 'r') as log:
    # linha2 = log.readline()
    
    sem_n = [linha[:-1] for linha in log.readlines()]
    
    # print(sem_n)
    # print(linha2)



