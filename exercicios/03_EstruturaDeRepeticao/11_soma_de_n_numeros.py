"""
Altere o programa anterior para mostrar no final a soma dos números.
"""
soma = 0
try:
    inicio = int(input('Digite o número inicial: ')) + 1
    fim = int(input('Digite o número final: '))
except ValueError:
    print('Não foi digitado um número inteiro.')
else:
    for x in range(inicio, fim):
        print(x)
        soma += x

    print(f'A soma é {soma}.')
