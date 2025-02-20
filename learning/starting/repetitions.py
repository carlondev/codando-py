# while

# condition = True

# while condition:
#     name = input('What your name? ')
#     print(f'Your name is {name}')

#     if name == 'quit':
#         break


counter = 0

while counter < 100:
    counter += 1

    if counter == 7:
        print("I don't show the 7.")
        continue

    if counter >= 10 and counter <= 30:
        print("I don't show the", counter)
        continue

    print(counter)

    if counter == 7:
        break

print('Finish.')

