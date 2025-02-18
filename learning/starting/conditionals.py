# if / elif     / else

action = input('Do you want to "go in" or "go out"? ')

if action == 'go in':
    print('You entered the system.')
    print('Welcome to the system!')
elif action == 'go out':
    print('You left the system.')
else:
    print('Invalid choice.')