"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
valor = float(input('Quanto você ganha por hora: '))
horas = float(input('Quantas horas você trabalhou no mês: '))
salario_bruto = valor * horas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato
print(f'Salário Bruto : R$ {salario_bruto:.2f}.')
print(f'IR : R$ {ir:.2f}.')
print(f'INSS : R$ {inss:.2f}.')
print(f'Sindicato : R$ {sindicato:.2f}.')
print(f'Salário Liquido : R$ {salario_liquido:.2f}.')
