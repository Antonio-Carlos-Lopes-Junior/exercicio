"""
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo,
por quais número ele é divisível.
"""
num_divisao = 0
divisores = []
while True:
    try:
        num = int(input('Digite o número para verificar se é primo: '))
    except ValueError:
        print('Digite um número')
    else:
        if num <= 1:
            print('Digite um número positivo maior que 1.')
        else:
            for n in range(2, num):
                resto = num % n
                if resto == 0:
                    num_divisao += 1
                    divisores.append(n)
            if num_divisao == 0:
                print(f'{num} é um número primo')
            else:
                print(f'{num} não é um número primo e é divisível por:')
                print('1', ', '.join([str(f'{divisor}') for divisor in divisores]), sep=', ', end=f' e {num}')
            break
