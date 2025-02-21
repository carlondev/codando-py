# while/else

team = 'LA Lakers'

i = 0
while i < len(team):
    letter = team[i]

    if letter == 'k':
        break

    print(letter)
    i += 1
else:
    print("I don't found letter k in the string.")