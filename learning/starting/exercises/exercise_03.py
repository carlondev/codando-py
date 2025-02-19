first_value = input('Enter a value: ')
second_value = input('Enter another value: ')

int_first_value = int(first_value)
int_second_value = int(second_value)

if int_first_value > int_second_value:
    print(f'{int_first_value=} is greater than {int_second_value=}')
elif int_first_value == int_second_value:
    print(f'{int_first_value=} is equal than {int_second_value=}')
else:
    print(f'{int_second_value=} is greater than {int_first_value=}')
