"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento  Conceito
Entre 9.0 e 10.0         A
Entre 7.5 e 9.0          B
Entre 6.0 e 7.5          C
Entre 4.0 e 6.0          D
Entre 4.0 e zero         E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o
conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""
try:
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
except ValueError:
    print('Você não digitou um número em algum momento.')
else:
    media = (nota1 + nota2) / 2
    if media >= 9:
        conceito = 'A'
    elif media >= 7.5:
        conceito = 'B'
    elif media >= 6:
        conceito = 'C'
    elif media >= 4:
        conceito = 'D'
    elif media >= 0:
        conceito = 'E'
    else:
        conceito = '"Valor inválido"'

    if conceito == 'A' or conceito == 'B' or conceito == 'C':
        mensagem = '"APROVADO"'
    elif conceito == 'D' or conceito == 'E':
        mensagem = '"REPROVADO"'
    else:
        mensagem = '"Valor inválido"'

    print(f'Suas notas foram {nota1:.1f} e {nota2:.1f}, '
          f'sua média foi {media:.1f}, '
          f'o conceito foi {conceito} '
          f'e você está {mensagem}.')
