"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 kg           Acima de 5 kg
File Duplo      R$ 4,90 por kg          R$ 5,80 por kg
Alcatra         R$ 5,90 por kg          R$ 6,80 por kg
Picanha         R$ 6,90 por kg          R$ 7,80 por kg
Para atender a todos os clientes, cada cliente poderá levar apenas um tipo de carne da promoção, porém
não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente
receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade
de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade
de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""
carne_str = ''
valor = 0
carne_tipo = input('Digite o Tipo de carne: F - Filé Duplo, A - Alcatra ou P - Picanha: ').upper()
if carne_tipo != 'F' and carne_tipo != 'A' and carne_tipo != 'P':
    print('Tipo de carne inválida.')
else:
    try:
        carne_peso = float(input('Digite quantos quilos vendido: '))
    except ValueError:
        print('Você não digitou um número.')
    else:
        if carne_peso <= 0:
            print('Peso inválido.')
        else:
            cartao = input('Será usado o cartão tabajara (S - Sim ou N - Não): ').upper()
            if cartao != 'S' and cartao != 'N':
                print('Informação inválida.')
            else:
                if carne_tipo == 'F':
                    if carne_peso > 5:
                        valor = carne_peso * 5.8
                    else:
                        valor = carne_peso * 4.9
                    carne_str = 'Filé Duplo'
                elif carne_tipo == 'A':
                    if carne_peso > 5:
                        valor = carne_peso * 6.8
                    else:
                        valor = carne_peso * 5.9
                    carne_str = 'Alcatra'
                elif carne_tipo == 'P':
                    if carne_peso > 5:
                        valor = carne_peso * 7.8
                    else:
                        valor = carne_peso * 6.9
                    carne_str = 'Picanha'

                print('A compra foi:')
                print(f'{carne_peso:.3f} kg de {carne_str} no valor de R$ {valor:.2f}')

                if cartao == 'S':
                    desconto = round(valor * 0.05, 2)
                    print('Será pago no cartão tabajara')
                    print(f'Desconto: R$ {desconto:.2f}.')
                else:
                    desconto = 0
                    print('Não será pago no cartão tabajara')

                valor -= desconto
                print(f'Valor final da compra R$ {valor:.2f}')
