"""
s - string
d and i - int
f - float
x and X - hexadecimal
.<number of digits>f
(character)(><^)(quantity)
> - left
< - right
^ - center
Signal - + or -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

team = 'Lakers'
print(f'{team}')
print(f'{team: >10}')
print(f'{team: <10}.')
print(f'{team: ^10}.')
print(f'{team:$^10}')
print(f'{12333.87548365973:.3f}')
