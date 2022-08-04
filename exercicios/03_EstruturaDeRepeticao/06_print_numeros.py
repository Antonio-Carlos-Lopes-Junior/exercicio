"""
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
Depois modifique o programa para ele mostrar os números um ao lado do outro.
"""
# Um abaixo do outro
print('Imprimindo um número abaixo do outro.')
num = 0
while num < 20:
    num += 1
    print(num)

# Um ao lado do outro
print('Imprimindo um número ao lado do outro.')
num = ''
i = 0
while i < 20:
    i += 1
    num += f'{str(i)}'
    if i < 21:
        num += f', '

print(num)

# Um ao lado do outro — lista
print('Imprimindo um número ao lado do outro - lista.')
num = []
i = 0
while len(num) < 20:
    i += 1
    num.append(i)

print(num)
