"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""
repetir = 'S'
while repetir == 'S':
    populacao_a = populacao_b = taxa_a = taxa_b = anos = 0
    while True:
        try:
            populacao_a = int(input('Digite a população do país A: '))
        except ValueError:
            print('Digite número.')
        else:
            if populacao_a > 0:
                break
            else:
                print('Digite um número maior que 0')

    while True:
        try:
            populacao_b = int(input('Digite a população do país B: '))
        except ValueError:
            print('Digite número.')
        else:
            if populacao_b > 0:
                break
            else:
                print('Digite um número maior que 0')

    while True:
        try:
            taxa_a = float(input('Digite a taxa de crescimento do país A: ')) / 100
        except ValueError:
            print('Digite número.')
        else:
            if taxa_a > 0:
                taxa_a += 1
                break
            else:
                print('Digite um número maior que 0')

    while True:
        try:
            taxa_b = float(input('Digite a taxa de crescimento do país B: ')) / 100
        except ValueError:
            print('Digite número.')
        else:
            if taxa_b > 0:
                taxa_b += 1
                break
            else:
                print('Digite um número maior que 0')

    anos = 0

    while populacao_a < populacao_b:
        populacao_a = int(populacao_a * taxa_a)
        populacao_b = int(populacao_b * taxa_b)
        anos += 1

    print(f'Levará {anos} anos para o país A ter uma população maior ou igual ao país B.')
    print(f'O pais A terá {populacao_a:,} pessoas')
    print(f'O pais B terá {populacao_b:,} pessoas')

    repetir = input('Quer repetir? S - Sim ou N - Não: ').upper()

    if repetir == 'N':
        break
    elif repetir != 'S':
        while repetir != 'S' and repetir != 'N':
            repetir = input('Digite S - Sim ou N - Não: ').upper()
