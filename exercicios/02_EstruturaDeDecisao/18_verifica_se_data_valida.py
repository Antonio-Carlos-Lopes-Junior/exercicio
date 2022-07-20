"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""
try:
    data = input('Digite uma data no formato dd/mm/aaaa: ')
    data_dia = int(data[slice(2)])
    data_mes = int(data[slice(3, 5)])
    data_ano = int(data[slice(-4, len(data))])
except ValueError:
    print('Data inválida.')
else:
    mes_31 = (1, 3, 5, 7, 8, 10, 12)
    mes_30 = (4, 6, 9, 11)
    mes_28_29 = 2
    if 0 < data_mes <= 12:
        if 0 < data_dia <= 28:
            print('Data válida.')
        elif data_dia == 29:
            if data_mes == mes_28_29 and (data_ano % 4) == 0 and (data_ano % 100) != 0 or (data_ano % 400) == 0:
                print('Data válida.')
            elif data_mes <= 12 and data_mes != mes_28_29:
                print('Data válida.')
            else:
                print('Data inválida.')
        elif data_dia == 30 and data_mes in mes_30:
            print('Data válida.')
        elif data_dia == 31 and data_mes in mes_31:
            print('Data válida.')
        else:
            print('Data inválida.')
    else:
        print('Data inválida.')
