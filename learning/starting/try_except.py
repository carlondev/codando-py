"""
try -> try to run the code
except -> an error occurred when trying to run

"""

num_str = input('I will double the number you enter: ')

try:
    num_float = float(num_str)
    print('FLOAT: ', num_float)
    print(f'Twice {num_str} é {num_float * 2}')
except:
    print('This is not a number.')