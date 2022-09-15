"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""
num_divisao = 0
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
            if num_divisao == 0:
                print(f'{num} é um número primo')
            else:
                print(f'{num} não é um número primo')
            break
