"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
a. par ou ímpar;
b. positivo ou negativo;
d. inteiro ou decimal.
"""
try:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    print('Que operação deseja realizar?')
    operacao = int(input('Digite 1 - Adição, 2 - Subtração, 3 - Multiplicação ou 4 - Divisão: '))
except ValueError:
    print('Você não digitou um número.')
else:
    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    elif operacao == 4 and num2 != 0:
        resultado = num1 / num2
    else:
        resultado = f'Operação inválida'

    # Verificando se o resultado é inteiro ou decimal
    if resultado == round(resultado):
        eh_inteiro = f'inteiro'
        resultado = int(resultado)
    else:
        eh_inteiro = f'decimal'
        resultado = round(resultado, 2)

    # Verificando se o resultado da operação é par ou ímpar
    if eh_inteiro == 'inteiro':
        if resultado % 2 == 0:
            eh_par = f'par, {eh_inteiro}'
        else:
            eh_par = f'ímpar, {eh_inteiro}'
    else:
        eh_par = f'{eh_inteiro}'

    # Verificando se o resultado é positivo ou negativo
    if resultado < 0:
        eh_positivo = f'negativo'
    else:
        eh_positivo = f'positivo'

    # Estrutura para exibir a mensagem na tela com as devidas considerações
    if resultado == 'Operação inválida':
        print(resultado)
    else:
        print(f'O resultado da operação é {resultado} e ele é {eh_par} e {eh_positivo}.')
