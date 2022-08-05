"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
i = 1
num = []
soma = media = 0
while i <= 5:
    try:
        soma += (float(input(f'Digite o {i}º número: ')))
    except ValueError:
        print('Não foi digitado um número.')
    else:
        media = soma / i
        if 2 <= i < 5:
            print(f'Por enquanto a soma é {soma} e a média é {media}.')
        elif i == 5:
            print(f'Por fim a soma é {soma} e a média é {media}.')
        i += 1
