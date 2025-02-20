"""
Tendo como dados de entrada a altura de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58
"""

altura_pessoa = input('Insira sua altura em metros: ')

altura_pessoa_real = float(altura_pessoa)

peso_ideal = (72.7 * altura_pessoa_real) - 58

print(f'O seu peso ideal é: {peso_ideal:.2f} kg')
