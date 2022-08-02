"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 kg           Acima de 5 kg
Morango         R$ 2,50 por kg          R$ 2,20 por kg
Maçã            R$ 1,80 por kg          R$ 1,50 por kg
Se o cliente comprar mais de 8 kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda
um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em kg) de morangos e a
quantidade (em kg) de maçãs adquiridas e escreva o valor a ser pago pelo cliente.
"""
morango_float = maca_float = produtos_float = desconto = 0
try:
    morango_float = float(input('Digite quantos kilos de morango vendido: '))
    if morango_float < 0:
        print('Quantidade inválida.')
    else:
        maca_float = float(input('Digite quantos kilos de maçã vendido: '))
        if maca_float < 0:
            print('Quantidade inválida.')
    morango_str = maca_str = produtos_str = ''
except ValueError:
    print('Você não digitou um número.')
else:
    if morango_float < 0 or maca_float < 0:
        pass
    else:
        if morango_float > 5:
            valor_morango = morango_float * 2.2
        else:
            valor_morango = morango_float * 2.5

        if maca_float > 5:
            valor_maca = maca_float * 1.5
        else:
            valor_maca = maca_float * 1.8

        if morango_float != 0 or maca_float != 0:
            print('A compra foi:')
            if morango_float != 0:
                print(f'{morango_float:.3f} Kg de Morango no valor de R$ {valor_morango:.2f}.')
                produtos_float += morango_float

            if maca_float != 0:
                print(f'{maca_float:.3f} Kg de Maçã no valor de R$ {valor_maca:.2f}.')
                produtos_float += maca_float

            valor_total = valor_morango + valor_maca

            if valor_total >= 25 or produtos_float >= 8:
                desconto = valor_total * 0.1
                print(f'Desconto: R$ {desconto:.2f}.')

            valor_total -= desconto

            print(f'Valor total à pagar: R$ {valor_total:.2f}')
