'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''
sexo = input('Digite seu sexo. "M" para Masculino, "F" para Feminino ou "I" para Indefinido: ').upper()
if sexo == 'M':
    print('Masculino')
elif sexo == 'F':
    print('Feminino')
elif sexo == 'I':
    print('Indefinido')
else:
    print('Sexo Inválido')
