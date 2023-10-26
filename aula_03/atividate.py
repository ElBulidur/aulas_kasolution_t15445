"""
 ===> Laboratório 3 - página 118 <===
    
    Em um clube, o valor da entrada varia de acordo com a idade do associado.
    Os critérios são:
    
    => Até 17 anos - R$ 50,00; 
    => Entre 18 e 59 anos - R$ 60,00;
    => A partir de 60 anos - R$ 20,00.
    
    O programa deve apresentar o nome do associado e o valor do ingresso a ser pago.
    
"""

def associado(x):
    print(f"Associado {x}")
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    if idade < 18:
        ingresso = 50.0
    elif idade < 60:
        ingresso = 60.00
    else:
        ingresso = 20.00
        
    return f"Associado: {nome}, Idade: {idade}, Valor do ingresso: {ingresso}"

# [print(y) for y in [associado({x+1}) for x in range(3)]]

# [print(j) for j in [1,2,3]]

# print(j) para j in [1]


# for j in [1,2,3]: # j=1 print(1) 
#     print(j)

# numero = [associado({x+1}) for x in range(2)]




"""
    ===> Laboratório 4 - página 119 <===
        
        Neste laboratório deverá ser usado o conceito de expressão if.
        Com base no ano fornecido pelo usuário, verificar se o ano é bissexto ou não, 
        e apresentar o número de dias referente ao mês de fevereiro.
    
"""

ano = int(input("Coloque o ano de referencia: "))
print(f"Ano Bissexto, Dias de fevereiro: 29") if ano%4 == 0 else print(f"Dias de fevereiro: 28")

# if ano % 4 == 0:
#     print(f"Ano Bissexto, Dias de fevereiro: 29")
# else:
#     print(f"Dias de fevereiro: 28")



    


