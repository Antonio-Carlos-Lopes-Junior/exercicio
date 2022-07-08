'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de
Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''
arquivo = float(input('Qual o tamanho do arquivo que quer fazer download: '))
velocidade = int(input('Qual a velocidade da internet: ')) / 8
download_minuto = (arquivo / velocidade) / 60
download_segundo = (arquivo / velocidade) % 60
print(f'O tempo aproximado para o download é de {download_minuto:.0f} minuto(s) e {download_segundo:.0f} segundo(s)')

