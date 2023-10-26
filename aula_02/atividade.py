"""
Laboratório 2

Escrever um programa que solicite ao usuário:

O nome de um funcionário;
Seu salário.

Se o salário for superior a R$ 5.000,00 ele terá um desconto de 10% sobre o que ultrapassar R$ 5.000,00. No final, apresentar:

O nome do funcionário;
O salário bruto;
O valor do desconto;
O salário líquido.

"""

# salario = 7000 (2000 * 10 / 100)

funcionario = input("Qual funcionario: ")
salario = float(input(f"Qual o salario do {funcionario}: "))

# salario_liquido = salario

if salario > 5000:
    desconto = (salario - 5000) * 10 / 100
else:
    desconto = 0.0
    
salario_liquido = salario - desconto

print(f"Funcionario: {funcionario}")
print(f"Salario Bruto: {salario}")
print(f"Descontos: {desconto}")
print(f"Salario Liquido: {salario_liquido}")







