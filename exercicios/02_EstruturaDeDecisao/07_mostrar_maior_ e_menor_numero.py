"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
"""
Opção 1 usando variáveis
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))
lista = [num1, num2, num3]
"""
# Opção 2 sem o uso de variáveis
try:
    lista = {int(input('Digite o primeiro numero: ')),
             int(input('Digite o segundo numero: ')),
             int(input('Digite o terceiro numero: '))}
except ValueError:
    print('Você não digitou um número em algum momento.')
else:
    lista_ordenada = sorted(lista)
    print(f'O maior numero é: {lista_ordenada[len(lista_ordenada)-1]}')
    print(f'O menor numero é: {lista_ordenada[0]}')
