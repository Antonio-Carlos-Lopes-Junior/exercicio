"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
— até 20 litros, desconto de 3% por litro
— acima de 20 litros, desconto de 5% por litro
Gasolina:
— até 20 litros, desconto de 4% por litro
— acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo do combustível (codificado da seguinte
forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do
litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""
try:
    litros = float(input('Digite quantos litros foi vendido: '))
    tipo = ''
    if litros < 0:
        print('Quantidade de litros inválida.')
    else:
        print('Que combustível foi vendido?')
        tipo = input('Digite A-álcool, G-gasolina: ').upper()
except ValueError:
    print('Você não digitou um número.')
else:
    if litros < 0:
        pass
    else:
        if tipo != 'A' and tipo != 'G':
            print('Tipo de combustível errado.')
        else:
            preco = 0
            desconto = 0
            if tipo == 'A':
                preco = 1.9
                tipo = 'Álcool'
                if litros <= 20:
                    desconto = 0.03
                else:
                    desconto = 0.05
            elif tipo == 'G':
                preco = 2.5
                tipo = 'Gasolina'
                if litros <= 20:
                    desconto = 0.04
                else:
                    desconto = 0.06
            valor_pagar = preco * (1 - desconto) * litros
            if litros == 1:
                print(f'O Valor a ser pago por {litros} litro de {tipo} é de R$ {valor_pagar:.2f}.')
            else:
                print(f'O Valor a ser pago por {litros} litros de {tipo} é de R$ {valor_pagar:.2f}.')
