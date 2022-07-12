"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
from unidecode import unidecode

letra = str(input('Digite uma letra: '))
vogal = ('a', 'e', 'i', 'o', 'u')
if letra == '':
    print('Você não digitou nada.')
elif not letra.isalpha():
    print('Você não digitou uma letra.')
elif len(letra) != 1:
    print('Digite uma e somente uma letra.')
elif unidecode(letra.lower()) in vogal:
    print('A letra é uma vogal.')
else:
    print('A letra é uma consoante.')
