import os, sys

requirements = 'requirements.txt'
pasta = '../aula_05'
# pasta = r'..\aula_05'

# print(os.path.exists(f"{pasta}/{requirements}"))
res = os.path.exists("../aula_06/requirements.txt")

# if res:
#     print("Existe o arquivo!!!")
# else:
#     print("Arquivo faltando!!!")


# print(os.path.isfile("../aula_05/requirements.txt")) #Verifica se e arquivo
# print(os.path.isdir("../aula_05")) # verifica se e pasta

raiz_app = 'C:/aula_python/aulas_kasolution_t15445/'

# if not os.getcwd() == raiz_app: os.chdir(raiz_app) # exemplo de uso do getcwd

# print(os.getcwd()) # saber local atual
# print(os.chdir('c:/')) # acessar novos locais
# print(os.getcwd())

# print(os.mkdir('manutencoes')) # cria pasta
# print(os.rmdir('manutencoes')) #deleta pasta
# print(os.listdir('../aula_05'))


# Exemplo de uso
# arquivos = 0
# pastas = 0

# for info in os.listdir('../aula_05'):
#     if os.path.isfile(f'../aula_05/{info}'):
#         arquivos += 1
#     else:
#         pastas += 1
        
# print(f"Tem {arquivos} arquivos e {pastas} pastas")

# os.system() # executa comando do terminal # ver porque o vscode esta usando o cmd e power shell.


# print(sys.platform)

# if sys.platform == 'win32':
#     os.system("")

# os.system("touch julio.txt")


#csv
import csv

alunos = [
    ['Julio', 'julio@email.com'],
    ['Cezar', 'cezar@email.com']
]

# with open('alunos.csv', 'w') as file_csv:
#     gravar = csv.writer(file_csv)# delimiter=';'
#     gravar.writerow(['Nome', 'Email'])
#     gravar.writerows(alunos)


with open('alunos.csv', 'r') as file_csv:
    arquivo_lido = csv.reader(file_csv)# delimiter=';'
    
    colunas = []
    linhas = []
    
    for i, linha in enumerate(arquivo_lido):
        if i == 0:
            colunas = linha
        else:
            if len(linha) > 0:
                linhas.append(linha)
            
    # print(colunas)
    # print(linhas)
    
# excel
import openpyxl

pasta_trabalho = openpyxl.load_workbook(filename='escola.xlsx')

produtos = []
total = 0

for i, linha in enumerate(pasta_trabalho['produtos'].iter_rows(values_only=True)):
    if i > 0:
        produtos.append(linha[0])
        total += linha[1]
    
print(f"Produtos: {produtos}")
print(f"total dos produtos: {total}")
    
    



    
    










