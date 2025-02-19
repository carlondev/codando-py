name = input('Enter your name: ')
age = input('Enter your age: ')

#bool_name = bool(name)
#bool_age = bool(age)

#if bool_name and bool_age == True:
if name and age:
    print(f'Your name is {name}')
    print(f'Your reversed name is {name[-1:-16:-1]}')
    if " " in name:
        print(f'Your name contains space.')
    else:
        print(f'Your name does not contain spaces.')
    print(f'Your name contain {len(name)} letters')
    print(f'The first letter in your name is {name[0]}')
    print(f'The last letter in your name is {name[-1]}')
else:
    print(f'Sorry, you left fields empty.')
