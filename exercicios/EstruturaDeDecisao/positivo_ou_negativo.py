"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""
try:
    num = float(input('Digite um número: '))
except ValueError:
    print('Você não digitou um número')
else:
    if num < 0:
        print(f'O número {num} é Negativo.')
    else:
        print(f'O número {num} é Positivo.')
