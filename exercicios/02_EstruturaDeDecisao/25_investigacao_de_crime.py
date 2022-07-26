"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4
como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
print('Digite S - Sim ou N - Não para as perguntas abaixo:')
telefone = input('"Telefonou para a vítima?": ').upper()
local = input('"Esteve no local do crime?": ').upper()
mora = input('"Mora perto da vítima?": ').upper()
devia = input('"Devia para a vítima?": ').upper()
trabalho = input('"Já trabalhou com a vítima?": ').upper()

participacao = 0
entrada_errada = False

# Verificação se telefonou para a vítima
if telefone == 'S':
    participacao += 1
elif telefone == 'N':
    participacao += 0
else:
    entrada_errada = True

# Verificação se esteve no local do crime
if local == 'S':
    participacao += 1
elif local == 'N':
    participacao += 0
else:
    entrada_errada = True

# Verificação se mora perto da vítima
if mora == 'S':
    participacao += 1
elif mora == 'N':
    participacao += 0
else:
    entrada_errada = True

# Verificação se devia para a vítima
if devia == 'S':
    participacao += 1
elif devia == 'N':
    participacao += 0
else:
    entrada_errada = True

# Verificação se já trabalhou com a vítima
if trabalho == 'S':
    participacao += 1
elif trabalho == 'N':
    participacao += 0
else:
    entrada_errada = True

# Análise das respostas
if entrada_errada:
    print('Entrada inválida em algum momento. Impossível fazer análise.')
else:
    if participacao == 2:
        print('A pessoa é "Suspeita".')
    elif 3 <= participacao <= 4:
        print('A pessoa é "Cúmplice".')
    elif participacao == 5:
        print('A pessoa é o "Assassino".')
    else:
        print('A pessoa é "Inocente".')
