phrase = 'Python is a multi-paradigm programming language.'\
    'Python was created by Guido van Rossum.'

i = 0
appeared_more_often = 0
best_letter = ''

while i < len(phrase):
    current_letter = phrase[i]

    if current_letter == ' ':
        i += 1
        continue

    how_many_letter_appear = phrase.count(current_letter)

    if appeared_more_often < how_many_letter_appear:
        appeared_more_often = how_many_letter_appear
        best_letter = current_letter

    i += 1

print('The letter that appeared most often was '
      f'"{best_letter}", which appeared {appeared_more_often} times.')