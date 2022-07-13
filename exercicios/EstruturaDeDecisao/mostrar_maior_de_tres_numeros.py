"""
Faça um Programa que leia três números e mostre o maior deles.
"""
try:
    lista = [float(input('Digite o primeiro número: ')),
         float(input('Digite o segundo número: ')),
         float(input('Digite o terceiro número: '))]
except ValueError:
    print('Você não digitou um número em algum momento.')
else:
    lista_ordenada = sorted(lista)
    print(f'O maior número é: {lista_ordenada[len(lista_ordenada)-1]}')
