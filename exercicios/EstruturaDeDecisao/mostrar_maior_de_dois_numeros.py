"""
Faça um Programa que peça dois números e imprima o maior deles.
"""
try:
    lista = [int(input('Digite o primeiro número: ')),
         int(input('Digite o segundo número: '))]
except ValueError:
    print('Você não digitou um número em algum momento.')
else:
    lista_ordenada = sorted(lista)
    print(f'O maior número é: {lista_ordenada[len(lista_ordenada)-1]}')
