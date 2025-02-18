a = 'AAA'
b = 'BBBBB'
c = 7.74325
string = 'a={name_1} b={name_2} c={name_3:.2f}'
format = string.format(name_1=a, name_2=b, name_3=c)


print(format)