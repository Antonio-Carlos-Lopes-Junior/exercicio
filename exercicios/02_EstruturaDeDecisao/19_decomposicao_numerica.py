"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e
unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com:
326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
try:
    num = int(input('Digite um número menor que 1000: '))
except ValueError:
    print('Não é um número.')
else:
    centena_str = dezena_str = unidade_str = ''
    partes_numericas = 0
    if num <= 0 or num >= 1000:
        print('Digite um valor entre 0 e 1000.')
    else:
        centena_int = int(num / 100)
        dezena_int = int((num - (centena_int * 100)) / 10)
        unidade_int = int(num % 10)
        if centena_int == 1:
            centena_str = '1 centena'
            partes_numericas += 1
        elif centena_int > 1:
            centena_str = f'{centena_int} centenas'
            partes_numericas += 1

        if dezena_int == 1:
            dezena_str = '1 dezena'
            partes_numericas += 1
        elif dezena_int > 1:
            dezena_str = f'{dezena_int} dezenas'
            partes_numericas += 1

        if unidade_int == 1:
            unidade_str = '1 unidade'
            partes_numericas += 1
        elif unidade_int > 1:
            unidade_str = f'{unidade_int} unidades'
            partes_numericas += 1

        if partes_numericas == 3:
            print(f'{centena_str}, {dezena_str} e {unidade_str}')
        elif partes_numericas == 1:
            print(f'{centena_str + dezena_str + unidade_str}')
        else:
            if centena_str != '':
                segunda_parte = f'{dezena_str + unidade_str}'
                print(f'{centena_str} e {segunda_parte}')
            else:
                print(f'{dezena_str} e {unidade_str}')
