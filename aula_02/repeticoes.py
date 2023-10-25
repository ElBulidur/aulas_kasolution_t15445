lista = [1,2,3,5,6]

tamanho = len(lista)


for i in lista:
    pass
    # print(i)
    
# print(range(2,tamanho))

cliente = {}

for chave, valor in [('nome','Julio'), ('sobrenome','Pereira')]:
    cliente[chave] = valor
    # break

for x in range(1, 10,3):
    pass
    # print(x)
    
    
for numero in range(6): 
    pass
    # if numero % 2 == 0:
        # print("Par")
    # else:
        # print(numero)


x = 0

while x < 2:
    # print("menor que 2")
    x = x + 1
    

multiplo_5 = False
tentativa = 0

while multiplo_5 == False: 
    # pegar saque
    saque = int(input("Coloque um valor multiplo de 05: "))
    
    if saque % 5 == 0:
        multiplo_5 = True
    else: 
        tentativa += 1
        
        if tentativa == 3:
            saque = "acabou as tentativas!!!"
            break
            
        print("Precisa ser multiplo de 5, tente novamente.")
        
# print(saque)

numeros = [1,2,3,4,'Julio']

novos_numeros = [x for x in numeros if x == 'Julio']

print(novos_numeros)
    
                
    
