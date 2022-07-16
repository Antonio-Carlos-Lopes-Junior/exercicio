# Faça um Programa que converta metros para centímetros.
try:
    metro = float(input('Digite quantos metros quer converter: '))
except ValueError:
    print('Você não digitou um número.')
else:
    print(f'O valor convertido é {metro * 100} cm')
