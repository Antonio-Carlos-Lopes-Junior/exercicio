"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 e 10.
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
"""
try:
    tabuada = int(input('Digite a tabuada de que número deseja ver: '))
except ValueError:
    print('Número inválido')
else:
    print(f'Tabuada de {tabuada}:')
    for x in range(1, 11):
        produto = tabuada * x
        print(f'{tabuada} X {x} = {produto}')
