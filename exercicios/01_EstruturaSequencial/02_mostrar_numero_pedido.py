# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
try:
    num = float(input('Digite um número: '))
except ValueError:
    print('Você não digitou um número.')
else:
    print(f'O número informado foi {num}.')
