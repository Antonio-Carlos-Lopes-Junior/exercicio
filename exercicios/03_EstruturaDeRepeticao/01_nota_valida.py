"""
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""
nota = -1
while nota < 0 or nota > 10:
    try:
        nota = float(input('Digite uma nota entre 0 e 10: '))
    except ValueError:
        print('Não foi digitado um número.')

print(f'A nota digitada foi: {nota:.1f}')
xxx
