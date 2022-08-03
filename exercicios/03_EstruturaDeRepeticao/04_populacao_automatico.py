"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse
ou iguale a população do país B, mantidas as taxas de crescimento.
"""
populacao_a = 80000
populacao_b = 200000
anos = 0

while populacao_a < populacao_b:
    populacao_a = int(populacao_a * 1.03)
    populacao_b = int(populacao_b * 1.015)
    anos += 1

print(f'Levará {anos} anos para o país A ter uma população maior ou igual ao país B.')
print(f'O pais A terá {populacao_a:,} pessoas')
print(f'O pais B terá {populacao_b:,} pessoas')
