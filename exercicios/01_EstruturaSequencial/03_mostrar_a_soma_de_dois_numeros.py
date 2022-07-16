# Faça um Programa que peça dois números e imprima a soma.
# Modo 1
num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')
try:
    print(f'A soma dos números é {int(num1) + int(num2)}')
except ValueError:
    print('Você não digitou um número em algum momento.')
else:
    print(f'A soma dos números é {int(num1) + int(num2)}')

# Modo 2
try:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
except ValueError:
    print('Você não digitou um número em algum momento.')
else:
    print(f'A soma dos números é {num1 + num2}')
