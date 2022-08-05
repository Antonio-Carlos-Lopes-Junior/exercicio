"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo
número. Não utilize a função de potência da linguagem.
"""
resultado = 1
try:
    base = float(input('Digite a base: '))
    expoente = int(input('Digite o expoente: '))
except ValueError:
    print('Número inválido.')
else:
    if expoente < 0:
        for x in range(expoente, 0):
            resultado *= base
        resultado = 1 / resultado
    elif expoente == 0:
        print('O resultado é 1')
    else:
        for x in range(expoente):
            resultado *= base

    print(resultado)
