"""
Tendo como dado de entrada a altura (h) de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""

altura = input('Insira sua altura em metros: ')
altura_float = float(altura)

genero = input('Você é [H]omem ou [M]ulher?: ').strip().lower()

if genero == 'h':
    peso_ideal = (72.7 * altura_float) - 58
elif genero == 'm':
    peso_ideal = (62.1 * altura_float) - 44.7
else:
    peso_ideal = None

if peso_ideal is not None:
    print(f'O seu peso ideal é: {peso_ideal:.2f}')
else:
    print('Entrada inválida! Digite H para homem e M para mulher.')


