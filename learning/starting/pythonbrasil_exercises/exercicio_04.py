"""
João Papo-de-Pescador, homem de bem, 
comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.
"""

peso = float(input('Insira o peso do peixe pescado em kg: '))

while peso <= 0:
    print('Peso inválido! O peso deve ter um valor positivo.')
    peso = float(input('Insira o peso do peixe pescado em kg: '))
    

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f'O peso excedente é de {excesso:.2f} kg.')
    print(f'Você deverá pagar uma multa de R${multa:.2f}.')
else:
    print(f'O peso está dentro do limite permitido. Não há excedente de peso.')
