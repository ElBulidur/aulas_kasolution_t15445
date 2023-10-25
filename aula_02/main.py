"""
Laboratório 02 - Página 117
    
    Suponha que em um caixa eletrônico existam cédulas disponíveis de 5, 10, 20 e 50 reais. 
    Usando operações de divisão inteira e resto da divisão, escrever um programa que solicite ao usuário um valor para saque e, 
    a partir deste valor, armazenar em variáveis e apresentar na tela a quantidade de cada cédula para compor o valor do saque.
    
    Obs.: Considerar neste exercício que os valores sejam sempre múltiplos de 5. Considerar também a menor quantidade possível de cédulas.

"""

saque = int(input("Digite o valor para saque (Multiplo de 5): ")) # 135

if saque % 5 != 0:
    print("por favor somente multiplo de 5")
else: 
    print("")
    print('='*20)
    print("")

    cedula_50 = saque // 50 # 2
    resto = saque % 50 # 35

    cedula_20 = resto // 20 
    resto = resto % 20

    cedula_10 = resto // 10
    resto = resto % 10

    cedula_5 = resto // 5

    print(f"Valor do saque: {saque}")
    print(f"{cedula_50} Cedulas de 50 \n {cedula_20} Cedulas de 20 \n{cedula_10}Cedulas de 10 \n{cedula_5} Cedulas de 5 \n")




