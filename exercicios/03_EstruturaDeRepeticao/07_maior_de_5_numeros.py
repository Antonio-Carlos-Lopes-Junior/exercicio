"""
Faça um programa que leia 5 números e informe o maior número.
"""
i = 1
num = []
while i <= 5:
    try:
        num.append(float(input(f'Digite o {i}º número: ')))
    except ValueError:
        print('Não foi digitado um número.')
    else:
        i += 1

num.sort(reverse=True)
print(f'O maior número é {num[0]}')
