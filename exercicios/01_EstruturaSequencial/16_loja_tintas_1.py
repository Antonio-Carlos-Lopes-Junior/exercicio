"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta
é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta
a serem compradas e o preço total.
"""
import math
try:
    area = float(input('Qual a área a ser pintada: '))
except ValueError:
    print('Você não digitou um número.')
else:
    litro_por_metro = 3
    litro_por_lata = 18
    valor_da_lata = 80
    tinta = area / litro_por_metro
    lata = math.ceil(tinta / litro_por_lata)
    preco = lata * valor_da_lata
    print(f'Você deverá comprar {lata} lata(s) no valor total de R$ {preco:.2f}')
