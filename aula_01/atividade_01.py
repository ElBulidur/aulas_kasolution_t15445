"""
    EXERCICIO 01
    
    Escrever um programa em Python que solicite informações de três pessoas, 
    como nome, idade, peso e altura. Apresentar na tela estas informações de modo que permaneçam alinhados verticalmente. 
    Usar a formatação de interpolação.
"""

# dados PRIUMEIRA pessoa
nome_1 = input("Escreva o nome da PRIMEIRA PESSOA: ")
idade_1 = int(input("Idade da PRIMEIRA PESSOA: "))
peso_1 = float(input("Peso da PRIMIERA PESSOAL: "))
altura_1 = float(input("Altura da PRIMEIRA PESSOA: "))

# dados SEGUNDA pessoa
nome_2, idade_2 = input("Escreva o nome da SEGUNDA PESSOA: "), int(input("Idade da SEGUNDA PESSOA: "))
peso_2, altura_2 = float(input("Peso da SEGUNDA PESSOAL: ")), float(input("Altura da SEGUNDA PESSOA: "))

# dados TERCEIRA pessoa
pessoa_3 = input("Escreva o nome da TERCEIRA PESSOA: "), int(input("Idade da TERCEIRA PESSOA: ")), float(input("Peso da TERCEIRA PESSOAL: ")), float(input("Altura da TERCEIRA PESSOA: "))

print("="*30)

print(f"Nome 01: {nome_1}")
print(f"Idade 01: {idade_1}")
print(f"Peso 01: {peso_1}")
print(f"Altura 01: {altura_1}")

print("="*30)

print(f"Nome 02: {nome_2} \n Idade 02: {idade_2} \n Peso 02: {peso_2} \n Altura 02: {altura_2}")

print("="*30)

print(f"Nome 03: {pessoa_3[0]} \n Idade 03: {pessoa_3[1]} \n Peso 03: {pessoa_3[2]} \n Altura 03: {pessoa_3[3]}")

# print(type(idade_1))

# CONDICIONAL

if 0 == 1:
    pass
    # print(" verdadeira")
else:
    pass
    # print("Falsa")
    
# < 7 => Reprovado | >7.9 => Aprovado | Entre 7 - 7.9 Recuperacao

nota = 6.9

# if nota > 7.9:
#     print("Aprovado!")
# elif nota >= 7:
#     print("Recuperacao")
# else:
#     print("Reprovado!")

# print("Aprovado") if nota > 7 else print("Reprovado")