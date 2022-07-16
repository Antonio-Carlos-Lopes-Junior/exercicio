# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
try:
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    nota4 = float(input('Digite a quarta nota: '))
except ValueError:
    print('Você não digitou um número em algum momento.')
else:
    print(f'A média das notas é {(nota1 + nota2 + nota3 + nota4) / 4}')
