"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
"""
try:
    produto1 = float(input('Digite o preço do primeiro produto: '))
    produto2 = float(input('Digite o preço do segundo produto: '))
    produto3 = float(input('Digite o preço do terceiro produto: '))
except ValueError:
    print('Você não digitou um número em algum momento.')
else:
    if produto1 == produto2 == produto3:
        print(f'Os três produtos tem o mesmo valor de R$ {produto1:.2f}')
    elif produto1 == produto2 < produto3:
        print(f'O primeiro e o segundo produtos são os mais baratos no valor de R$ {produto1:.2f}')
    elif produto1 == produto3 < produto2:
        print(f'O primeiro e o terceiro produtos são os mais baratos no valor de R$ {produto1:.2f}')
    elif produto2 == produto3 < produto1:
        print(f'O segundo e o terceiro produtos são os mais baratos no valor de R$ {produto2:.2f}')
    elif produto1 < produto2 and produto1 < produto3:
        print(f'O primeiro produto é o mais barato no valor de R$ {produto1:.2f}')
    elif produto2 < produto3:
        print(f'O segundo produto é o mais barato no valor de R$ {produto2:.2f}')
    else:
        print(f'O terceiro produto é o mais barato no valor de R$ {produto3:.2f}')
