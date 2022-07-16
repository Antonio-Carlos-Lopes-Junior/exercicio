# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
try:
    lado = int(input('Digite o tamanho de um dos lados do quadrado: '))
except ValueError:
    print('Você não digitou um número.')
else:
    area = lado ** 2
    print(f'O dobro da área é {area * 2}')
