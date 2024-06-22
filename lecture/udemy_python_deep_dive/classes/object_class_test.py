 # [ Class & Instance ]

class Person:
    pass

 # - Class is 'Type' Object
print(type(Person))         # <class 'type'>

# - Class Attrbiute
print(Person.__name__)

# - Instance Type & Class
p = Person()
print(type(p))
print(p.__class__)

print(type(p) is p.__class__)
print(isinstance(p, Person))

print("------------------------------")

# [ Class Atributes ]
class Person:
    language = 'Python'
    version = '3.6'

# - get Attribute
print(getattr(Person, 'version'))
print(Person.version)

try:
    getattr(Person, 'no')
except AttributeError as e:
    print(e)

print(getattr(Person, 'no', 'default'))

# - set Attribute
setattr(Person, 'version', 3.7)
print(Person.version)
Person.version = 3.8
print(Person.version)
print(Person.__dict__)

# - delete Attrbiute
delattr(Person, 'version')
del Person.language
print(Person.__dict__)

print("------------------------------")
# [ Built-in Type Attributes ]
my_str = 'test'
try:
    my_str.test = 'value'
except AttributeError as e:
    print(e)

try:
    setattr(my_str, 'test', 'value')
except AttributeError as e:
    print(e)

print("------------------------------")

# [ Class __dict__ ]
# - Read
for item in Person.__dict__.items():
    print(item)

# - Update ?
# - Read Only (Not Real dict)
try:
    Person.__dict__['extra'] = 'test'
except TypeError as e:
    print(e)


