"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
try:
    lista = [int(input('Digite o primeiro numero: ')),
             int(input('Digite o segundo numero: ')),
             int(input('Digite o terceiro numero: '))]
except ValueError:
    print('Você não digitou um número em algum momento.')
else:
    lista_ordenada = sorted(lista)
    print(f'Os números em ordem decrescente são: {lista_ordenada[2]}, {lista_ordenada[1]} e {lista_ordenada[0]}.')
