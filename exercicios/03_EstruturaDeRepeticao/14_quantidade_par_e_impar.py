"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares
e a quantidade de números impares.
"""
x = par = impar = 0
while x < 10:
    try:
        numero = int(input(f'Digite o {x + 1}º número: '))
    except ValueError:
        print('Você não digitou um número.')
    else:
        x += 1
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1

if par != 1 and impar != 1:
    print(f'Você digitou {par} números pares e {impar} ímpares.')
elif par != 1:
    print(f'Você digitou {par} números pares e {impar} ímpar.')
else:
    print(f'Você digitou {par} número par e {impar} ímpares.')
