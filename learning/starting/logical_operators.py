# and / or / not

# ATTENTION!!! This is for studies only

entry = input('[E]nter [Q]uit: ')
passwd = input('Password: ')

passwd_allowed = '123456'

if (entry == 'E' or entry == 'e') and passwd == passwd_allowed:
    print('Entered')
else:   
    print('Leave')

print(not True)  # False
print(not False)  # True
