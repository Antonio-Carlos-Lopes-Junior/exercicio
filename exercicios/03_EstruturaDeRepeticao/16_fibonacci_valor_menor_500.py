"""
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.
"""
num1 = num2 = 0
x = 1
while num1 <= 500:
    print(num2)
    num1 = num2
    num2 = x
    x += num1
