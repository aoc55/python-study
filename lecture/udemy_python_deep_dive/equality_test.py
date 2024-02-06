# [ Immutable ]
a = 'hi'
b = 'hi'
print(a is b)           # Identity = True
print(a == b)           # Eqauilty = True

# [ Mutable ]
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)           # Identity = False
print(a == b)           # Eqauilty = True
