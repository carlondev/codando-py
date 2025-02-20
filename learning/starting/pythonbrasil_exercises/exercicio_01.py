"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""

num_1 = input('Insira um número inteiro: ')
num_2 = input('Insira outro número inteiro: ')
num_3 = input('Insira um número real: ')

num_1_inteiro = int(num_1)
num_2_inteiro = int(num_2)
num_3_real = float(num_3)

# Cálculos
resultado_1 = (num_1_inteiro * 2) * (num_2_inteiro / 2)
resultado_2 = (num_1_inteiro * 3) + num_3_real
resultado_3 = num_3_real ** 3

# Resultados
print(f'O produto do dobro do primeiro com metade do segundo: {resultado_1}')
print(f'A soma do triplo do primeiro com o terceiro: {resultado_2}')
print(f'O terceiro elevado ao cubo: {resultado_3:.2f}')

