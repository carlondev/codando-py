name = input('Enter your first name: ')

name_length = len(name)

if name_length <= 4:
    print('Your name is short!')
elif name_length >= 5 and name_length <= 6:
    print('Your name is normal!')
else:
    print('Your name is big!')