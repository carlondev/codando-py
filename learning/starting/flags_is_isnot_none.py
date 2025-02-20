"""
Flag -> mark a location
None -> no value
is and is not -> is or not is (type, value, identity)
id -> identity
"""

condition = True
passed_if = None

if condition:
    passed_if = True
    print('Do something.')
else:
    print("Don't do someting.")

print(passed_if, passed_if is None)
print(passed_if, passed_if is not None)
