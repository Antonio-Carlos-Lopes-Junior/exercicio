"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""
try:
    num = int(input('Digite o número para calcular o fatorial: '))
except ValueError:
    print('Valor errado.')
else:
    fatorial = 1
    if num < 0:
        print('Digite um valor positivo.')
    else:
        for x in range(1, num + 1):
            fatorial *= x
        print(f'O valor de {num}! é {fatorial}.')
