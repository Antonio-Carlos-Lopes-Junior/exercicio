"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""
num1 = 0
x = num2 = 1
while True:
    try:
        n = int(input('Quantos números da série Fibonacci quer saber? '))
    except ValueError:
        print('Digite um número inteiro.')
    else:
        if n < 1:
            print('Digite um número positivo.')
        else:
            for _ in range(n):
                print(num2)
                num1 = num2
                num2 = x
                x += num1
            break
