"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes
e limitando o fatorial a números inteiros positivos e menores que 16.
"""
while True:
    try:
        num = int(input('Digite o número para calcular o fatorial: '))
    except ValueError:
        print('Digite um número')
    else:
        if 0 <= num < 16:
            fatorial = 1
            if num < 0:
                print('Digite um valor positivo.')
            else:
                for x in range(1, num + 1):
                    fatorial *= x
                print(f'O valor de {num}! é {fatorial:,}.')
            print('Quer calcular outro fatorial?')
            while True:
                mais_numero = input('Digite S - Sim ou N - Não: ').upper()

                if mais_numero != 'N' and mais_numero != 'S':
                    print('Você não digitou S - Sim ou N - Não')
                else:
                    break
            if mais_numero == 'N':
                break
        else:
            print('Digite um número positivo menor que 16')
