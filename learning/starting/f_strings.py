name = 'Carlos Henrique'
height = 1.83
weight = 78
bmi = weight / height ** 2

print(name, 'is', height, 'tall, weighs', weight, 'kilos and his BMI is', bmi)

# f-strings
line_1 = f'{name} is {height:.2f} tall,'
print(line_1)
line_2 = f'weighs {weight} kilos and his BMI is'
print(line_2)
line_3 = f'{bmi:.2f}'
print(line_3)

