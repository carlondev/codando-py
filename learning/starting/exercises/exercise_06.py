team = "Los Angeles Lakers"

new_team = ""

counter = 0

while counter < len(team):
    new_team += team[counter]
    if counter < len(team) - 1:
        new_team += "*"
    counter += 1

print(new_team)

"""
while counter < len(team):
    letter = team[counter]
    new_team += f'*{letter}'
    counter += 1
"""