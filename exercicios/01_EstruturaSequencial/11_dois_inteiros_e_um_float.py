"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a. o produto do dobro do primeiro com metade do segundo.
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.
"""
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite mais um número inteiro: '))
num3 = float(input('Digite um número real: '))

produto = (num1 * 2) * (num2 / 2)
soma = (num1 * 3) + num3
cubo = num3 ** 3

print(f'O primeiro cálculo é {produto}')
print(f'O segundo cálculo é {soma:.2f}')
print(f'O terceiro cálculo é {cubo:.2f}')
