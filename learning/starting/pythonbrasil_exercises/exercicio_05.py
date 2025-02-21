"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

tamanho_arquivo = float(input('Informe o tamanho do arquivo a ser baixado em MB: '))
velocidade_internet = float(input('Informe a velocidade do seu link de Internet em Mbps: '))


while tamanho_arquivo <= 0 or velocidade_internet <= 0:
    print('Valores inválidos.')
    tamanho_arquivo = float(input('Informe o tamanho do arquivo a ser baixado em MB: '))
    velocidade_internet = float(input('Informe a velocidade do seu link de Internet em Mbps: '))

if tamanho_arquivo and velocidade_internet > 0:
    tempo_download = (tamanho_arquivo / (velocidade_internet / 8)) / 60
    print(f'O tempo estimado de download será de {tempo_download:.2f} minutos.')

