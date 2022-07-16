"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta
é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
-comprar apenas latas de 18 litros;
-comprar apenas galões de 3,6 litros;
-misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
import math

try:
      area = float(input('Qual a área a ser pintada: '))
except ValueError:
    print('Você não digitou um número.')
else:
      area_com_folga = area * 1.1
      litro_por_metro = 6
      litro_por_lata = 18
      litro_por_galao = 3.6
      valor_da_lata = 80
      valor_do_galao = 25
      tinta = area_com_folga / litro_por_metro
      lata = math.ceil(tinta / litro_por_lata)
      preco_lata = lata * valor_da_lata
      galao = math.ceil(tinta / litro_por_galao)
      preco_galao = galao * valor_do_galao
      print(f'Você deverá comprar {lata} lata(s) de 18 litros no valor total de R$ {preco_lata:.2f}')
      print(f'Você deverá comprar {galao} galão(ões) de 3,6 litros no valor total de R$ {preco_galao:.2f}')
      lata = math.floor(tinta / litro_por_lata)
      litro_restante = tinta % litro_por_lata
      galao = math.ceil(litro_restante / litro_por_galao)
      preco_combinado = lata * valor_da_lata + galao * valor_do_galao
      print(f'Você deverá comprar {lata} lata(s) de 18 litros '
            f'mais {galao} galão(ões) de 3,6 litros '
            f'no valor total de R$ {preco_combinado:.2f}')
