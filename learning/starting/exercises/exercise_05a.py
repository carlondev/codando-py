num = input('Enter a integer: ')

# int_num = int(num)


# if int_num % 2 == 0:
#     print(f'The number {int_num} is a even!')
# else:
#     print(f'The number {int_num} is odd!')

if num.isdigit():
    num_int = int(num)
    even_odd = num_int % 2 == 0
    even_odd_text = 'odd'

    if even_odd:
        even_odd_text = 'even'

    print(f'The number {num_int} is {even_odd_text}')
else:
    print("You didn't enter a whole number!")