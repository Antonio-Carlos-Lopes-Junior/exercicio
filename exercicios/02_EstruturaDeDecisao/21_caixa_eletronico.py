"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois
informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de
5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas
de 10, uma nota de 5 e quatro notas de 1.
"""
try:
    saque = int(input('Digite quanto quer sacar.(limite entre R$ 10,00 e R$ 600,00): '))
except ValueError:
    print('Você não digitou um número em algum momento.')
else:
    saque_100_str = saque_50_str = saque_10_str = saque_5_str = saque_1_str = ''
    partes_numericas = 0
    if saque < 10 or saque > 600:
        print('Valor de saque inválido.')
    else:
        print('O saque será de:')

        saque_100_int, saque = divmod(saque, 100)
        saque_100_int, saque = divmod(saque, 100)
        saque_50_int, saque = divmod(saque, 50)
        saque_10_int, saque = divmod(saque, 10)
        saque_5_int, saque_1_int = divmod(saque, 5)

        if saque_100_int == 1:
            saque_100_str = '1 nota de 100'
            partes_numericas += 1
        elif saque_100_int > 1:
            saque_100_str = f'{saque_100_int} notas de 100'
            partes_numericas += 1

        if saque_50_int == 1:
            saque_50_str = '1 nota de 50'
            partes_numericas += 1

        if saque_10_int == 1:
            saque_10_str = '1 nota de 10'
            partes_numericas += 1
        elif saque_10_int > 1:
            saque_10_str = f'{saque_10_int} notas de 10'
            partes_numericas += 1

        if saque_5_int == 1:
            saque_5_str = '1 nota de 5'
            partes_numericas += 1

        if saque_1_int == 1:
            saque_1_str = '1 nota de 1'
            partes_numericas += 1
        elif saque_1_int > 1:
            saque_1_str = f'{saque_1_int} notas de 1'
            partes_numericas += 1

        texto_unidade = f'{saque_5_str} e {saque_1_str}'
        parte_unidade = f'{saque_5_str + saque_1_str}'
        texto_dezena = f'{saque_50_str} e {saque_10_str}'
        parte_dezena = f'{saque_50_str + saque_10_str}'
        if partes_numericas == 5:
            print(f'{saque_100_str}, {saque_50_str}, {saque_10_str}, {saque_5_str} e {saque_1_str}')
        elif partes_numericas == 1:
            print(f'{saque_100_str + saque_50_str + saque_10_str}')
        elif partes_numericas == 4:
            if saque_100_str == '':
                print(f'{saque_50_str}, {saque_10_str}, {texto_unidade}')
            else:
                if saque_1_str == '' or saque_5_str == '':
                    print(f'{saque_100_str}, {saque_50_str}, {saque_10_str} e {parte_unidade}')
                else:
                    print(f'{saque_100_str}, {parte_dezena}, {texto_unidade}')
        elif partes_numericas == 3:
            if saque_100_str == '':
                if saque_50_str == '' or saque_10_str == '':
                    print(f'{parte_dezena}, {texto_unidade}')
                else:
                    print(f'{saque_50_str}, {saque_10_str} e {parte_unidade}')
            else:
                if saque_50_str == '' and saque_10_str == '':
                    print(f'{saque_100_str}, {texto_unidade}')
                elif saque_50_str == '' or saque_10_str == '':
                    print(f'{saque_100_str}, {parte_dezena} e {parte_unidade}')
                else:
                    print(f'{saque_100_str}, {texto_dezena}')
        else:
            if saque_100_str == '':
                if saque_5_str == '' and saque_1_str == '':
                    print(f'{texto_dezena}')
                elif saque_50_str == '' and saque_10_str == '':
                    print(f'{texto_unidade}')
                else:
                    print(f'{parte_dezena} e {parte_unidade}')
            else:
                if saque_5_str == '' and saque_1_str == '':
                    print(f'{saque_100_str} e {parte_dezena}')
                elif saque_50_str == '' and saque_10_str == '':
                    print(f'{saque_100_str} e {parte_unidade}')
