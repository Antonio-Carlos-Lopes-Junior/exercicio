"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""
while True:
    nome = input('Digite seu nome: ')

    if len(nome) > 3:
        break
    else:
        print('O nome tem que ter mais que três caracteres.')

while True:
    idade = 0
    try:
        idade = int(input('Digite sua idade: '))
    except ValueError:
        print('Digite um número.')
    else:
        if 0 <= idade <= 150:
            break
        else:
            print('A idade tem que ser entre 0 e 150.')

while True:
    salario = 0
    try:
        salario = int(input('Digite seu salário: '))
    except ValueError:
        print('Digite um número.')
    else:
        if salario > 0:
            break
        else:
            print('O salário tem que ser maior que 0.')

while True:
    sexo = input('Digite seu sexo (f - feminino ou m - masculino): ').lower()

    if sexo == 'f' or sexo == 'm':
        break
    else:
        print('Digite "f" ou "m" para seu sexo.')

# Estado Civil: 's', 'c', 'v', 'd';
while True:
    estado_civil = input('Digite seu estado civil (s - solteiro(a), c - casado(a),'
                         ' v - viúvo(a) ou d - divorciado(a)): ').lower()

    if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
        break
    else:
        print('Digite "s", "c", "v" ou "d" para seu estado civil.')
