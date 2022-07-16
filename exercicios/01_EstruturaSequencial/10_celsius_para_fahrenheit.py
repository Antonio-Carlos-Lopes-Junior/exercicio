# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
try:
    celsius = float(input('Digite a temperatura em Celsius: '))
except ValueError:
    print('Você não digitou um número.')
else:
    fahrenheit = ((celsius / 5) * 9) + 32
    print(f'A temperatura em Fahrenheit é {fahrenheit:.2f}.')
