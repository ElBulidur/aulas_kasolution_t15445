
# PROCEDURAL
a = 10
b = 100

# print(a+b)

# fUNCAO SOMAR
## sem retornar
def somar_sem_retorno():
    print("Realizando a soma...")
    print(a+b)
    
## retorna
def somar_retorna():
    return a+b


# somar_sem_retorno()

# resultado = somar_retorna()


## Com parametro
def somar_com_param(a, b):
    print(a+b)

# somar_com_param(2,9)

## parametro Padrao
def somar_com_param_padrao(num=10, b=10):
    print(num+b)
    
# somar_com_param_padrao()

# referencia
def deixa_maiusculo(texto:str):
    print(texto.upper())
    

#args
def somar_valores(salario, *descontos):
    print(salario)
    print(type(descontos))
    
# somar_valores(2, 5, 4,5,6,7,8)

#kargs
def somar_kvalores(**kargs):
    print(kargs)
    
# somar_kvalores(salario=200, desconto=300)



