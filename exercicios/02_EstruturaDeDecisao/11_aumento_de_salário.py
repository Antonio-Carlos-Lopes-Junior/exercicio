"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram
para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5%
Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
try:
    salario_atual = float(input('Digite o salário atual: '))
except ValueError:
    print('Você não digitou um número.')
else:
    if salario_atual <= 280:
        percentual = 0.2
    elif salario_atual <= 700:
        percentual = 0.15
    elif salario_atual <= 1500:
        percentual = 0.1
    else:
        percentual = 0.05
    valor_do_aumento = salario_atual * percentual
    salario_novo = salario_atual + valor_do_aumento
    print(f'O salário atual é R$ {salario_atual:.2f}')
    print(f'O percentual aplicado foi {percentual * 100:.0f}%')
    print(f'O aumento será de R$ {valor_do_aumento:.2f}')
    print(f'O salário novo é R$ {salario_novo:.2f}')
