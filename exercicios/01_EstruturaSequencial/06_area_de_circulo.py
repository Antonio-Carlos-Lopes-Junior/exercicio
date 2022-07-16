# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

try:
    raio = float(input('Digite o raio do círculo: '))
except ValueError:
    print('Você não digitou um número.')
else:
    area = math.pi * raio ** 2
    print(f'A área do círculo é {area:.2f}.')
