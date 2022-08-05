"""
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo
compreendido por eles.
"""
try:
    inicio = int(input('Digite o número inicial: ')) + 1
    fim = int(input('Digite o número final: '))
except ValueError:
    print('Não foi digitado um número inteiro.')
else:
    for x in range(inicio, fim):
        print(x)
