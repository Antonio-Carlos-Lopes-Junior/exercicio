'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
a.Para homens: (72.7*h) - 58
b.Para mulheres: (62.1*h) - 44.7'''
altura = float(input('Digite sua altura em metros: '))
peso_h = (72.7 * altura) - 58
peso_m = (62.1 * altura) - 44.7
print(f'Seu peso ideal se você for homem {peso_h:.3f} Kg')
print(f'Seu peso ideal se você for mulher {peso_m:.3f} Kg')
