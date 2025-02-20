time = input('What time is it?')

time_int = int(time)

morning = time_int >= 0 and time_int <= 11
afternoon = time_int >= 12 and time_int <= 17
night = time_int >= 18 and time_int <= 23

if morning:
    print('Good morning!')
elif afternoon:
    print('Good afternoon!')
elif night:
    print('Good night!')
else:
    print('Invalid time.')