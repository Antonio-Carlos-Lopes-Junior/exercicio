"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes
situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer
pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
try:
    a = int(input('Digite o "a" da equação: '))
    if a == 0:
        print('Não é uma equação do segundo grau.')
    else:
        b = int(input('Digite o "b" da equação: '))
        c = int(input('Digite o "c" da equação: '))
except ValueError:
    print('Você não digitou um número em algum momento.')
else:
    if a == 0:
        pass
    else:
        delta = (b ** 2) - (4 * a * c)
        if delta < 0:
            print('Não possui raízes reais')
        elif delta == 0:
            raiz = -b / (2 * a)
            print(f'A raiz da equação é {raiz}.')
        else:
            raiz1 = (-b + (delta ** (1 / 2))) / (2 * a)
            raiz2 = (-b - (delta ** (1 / 2))) / (2 * a)
            print(f'As raízes são {raiz1} e {raiz2}.')
