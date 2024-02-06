# [Immutable]
a = 10
b = 10
print(id(a), id(b), id(a) == id(b))  # True

# [Immutable 2]
a = "abc"
b = "abc"
print(id(a), id(b), id(a) == id(b))  # True

# [Mutable]
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a), id(b), id(a) == id(b))  # False


