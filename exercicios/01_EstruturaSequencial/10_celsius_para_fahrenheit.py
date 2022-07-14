# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = ((celsius / 5) * 9) + 32
print(f'A temperatura em Fahrenheit é {fahrenheit:.2f}.')
