# calculator with while

while True:
    num_1 = input('Enter a number: ')
    num_2 = input('Enter another number: ')
    operator = input('Enter a operator (+ - / *): ')
    
    valid_numbers = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        valid_numbers = True
    except:
        valid_numbers = None

    if valid_numbers is None:
        print('One or both of the numbers entered are not valid.')
        continue

    allowed_operators = '+-*/'

    if operator not in allowed_operators:
        print('Invalid operator.')
        continue

    if len(operator) > 1:
        print('Enter only one operator.')
        continue

    if operator == '+':
        print('The result is:', num_1_float + num_2_float)
    elif operator == '-':
        print('The result is:', num_1_float - num_2_float)
    elif operator == '*':
        print('The result is:', num_1_float * num_2_float)
    else:
        print('The result is:', num_1_float / num_2_float)


    quit = input('Want to get out of the calculator? [Y]es: ').lower().startswith('y')
 
    if quit is True:
        break