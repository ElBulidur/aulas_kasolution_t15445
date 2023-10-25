

numeros = 12, "julio"


# ===== COLECOES ===== (mutavel ou imutavel | retorna ou nao valores)

# LISTA => list => MUTAVEL (MUDA)

aluno = ['Andre', 18, 1.97, True, [6,7,3,6,]]

# aluno.append(" Aprovado") # adiciona (Nao retorna)

# aluno[4].append("Aprovado")

# aluno[4][2] = 8

# aluno.clear() # limpa a lista (nao retorna)

vezes = aluno[4].count(6) # retorna as vezes repetida (retorna)

# nome = aluno.pop(0) # remove o elemento da posicao (Retorna)

# aluno.reverse()
# aluno.insert(1, "Dados")

resultado = aluno.index(18) # saber a posicao do valor (Retorna)

# print(type(aluno))


# DICIONARIO => dict ========= Mutavel

aluno_julio = {
    'nome': 'Julio',
    'sobrenome': 'Pereira',
    'idade': 18,
    'altura': 1.92,
    'Notas': {
        '1Bim': 10,
        '2Bim': 8,
        '3Bim': 6,
        '4Bim': 4,
    }
}

# print(aluno_julio)

nome = aluno_julio['nome']

sobrenome = aluno_julio.get('Sobrenome')

# aluno_julio['nome'] = 'Cezar' # Alterando valor

# print(aluno_julio.keys())
# print(aluno_julio.values())
# print(aluno_julio.items())
# print(type(aluno_julio))

# print(nome)
# print(sobrenome)


# TUPLA tuple ====> IMUTAVEL

lista = [1,2,3]
dicionario = {'chave': 'valor'}
tupla = (1,2,3)

dias_semana = ('Seg', 'Ter', 'Qua', 'Qui', 'Sex')

lista[0] = 10

# tupla[0] = 10

# print(aluno_julio.items())
