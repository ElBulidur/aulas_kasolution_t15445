# import random as rd
from random import randint, randrange

from calculadora import somar, subtrair, mult, divisao

from calc import somar
# num = randint(0,34)
# num2 = randrange(0, 20, 4)
# print(num)
# print(num2)

### CALCULADORA

def start():
    print("====== calculador do julio ==========")
    print("Bem vindo a minha calculadora, escolha uma das opcoes abaixo:")
    print("")


    print("A = SOMA")
    print("B = SUBTRACAO")
    print("C = MULTIPLICACAO")
    print("D = DIVISAO")


    a = int(input("Numero 01: "))
    b = int(input("Numero 02: "))

    opcao = input("Escolha a opcao desejada: ").lower()
    print("")

    if opcao == 'a':
        escolha = 'Soma'
        resultado = somar(a, b)
    elif opcao =='b':
        escolha = 'Subtracao'
        resultado = subtrair(a, b)
    elif opcao == 'c':
        escolha = 'Multiplicacao'
        resultado = mult(a, b)
    elif opcao == 'd':
        escolha = 'Divisao'
        resultado = divisao(a, b)
    else:
        print("Escolha errada!!!")
        print("saindo...")
        

    print(f"Resultado da {escolha}: {resultado}")

if __name__ == '__main__':
    pass
    # start()