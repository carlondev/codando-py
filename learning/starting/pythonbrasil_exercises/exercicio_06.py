"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
 O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
 Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
 entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
 Caso contrário, ele será classificado como "Inocente".
"""

print('Você está sob investigação! Responsa as próximas perguntas apenas com "sim" ou "não": ')

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas_positivas = 0

for pergunta in perguntas:
    resposta = input(pergunta + ' (s/n): ').strip().lower()
    if resposta[0] == 's':
        respostas_positivas += 1

if respostas_positivas == 2:
    classificacao = 'Suspeita'
elif 3 <= respostas_positivas <= 4:
    classificacao = 'Cúmplice'
elif respostas_positivas == 5:
    classificacao = 'Assassino'
else:
    classificacao = 'Inocente'

print(f'Classificação: {classificacao}')

