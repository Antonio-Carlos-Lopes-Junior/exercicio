"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""
try:
    lado1 = int(input('Digite o primeiro lado: '))
    lado2 = int(input('Digite o segundo lado: '))
    lado3 = int(input('Digite o terceiro lado: '))
except ValueError:
    print('Você não digitou um número em algum momento.')
else:
    if (lado1 + lado2) <= lado3 or (lado1 + lado3) <= lado2 or (lado2 + lado3) <= lado1:
        print('Não pode ser triângulo')
    else:
        if lado1 == lado2 == lado3:
            print('Esse é um triângulo equilátero')
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print('Esse é um triângulo isósceles')
        else:
            print('Esse é um triângulo escaleno')
