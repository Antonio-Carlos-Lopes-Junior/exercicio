'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.'''
valor = float(input('Quanto você ganha por hora: '))
horas = float(input('Quantas horas você trabalhou no mês: '))
print(f'O seu salario é R$ {valor * horas:.2f}.')
