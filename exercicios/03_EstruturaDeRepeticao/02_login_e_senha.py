"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""
# Primeira tentativa
"""
login = input('Digite seu login: ')
senha = input('Digite sua senha: ')

while login == senha:
    print('Login e senha não pode ser igual')
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')
"""
# Segunda tentativa
while True:
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')

    if login == senha:
        print('Login e senha não pode ser igual')
    else:
        break
