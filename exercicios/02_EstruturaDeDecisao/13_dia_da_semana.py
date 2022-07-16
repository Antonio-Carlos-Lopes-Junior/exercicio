"""
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""
# feito por if
try:
    numero = int(input('Digite um número para a semana: '))
except ValueError:
    print('Você não digitou um número')
else:
    if numero == 1:
        print('Domingo')
    elif numero == 2:
        print('Segunda')
    elif numero == 3:
        print('Terça')
    elif numero == 4:
        print('Quarta')
    elif numero == 5:
        print('Quinta')
    elif numero == 6:
        print('Sexta')
    elif numero == 7:
        print('Sábado')
    else:
        print('Valor inválido.')

# Feito por dicionário
"""
dia_da_semana = {}
numero = 0
try:
    numero = int(input('Digite um número para a semana: '))
except ValueError:
    pass
else:
    dia_da_semana = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado'
    }
try:
    calculo_da_semana = dia_da_semana[numero]
except KeyError:
    print('Valor inválido.')
else:
    print(calculo_da_semana)
"""
