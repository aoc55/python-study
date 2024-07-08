# [ 'object' is class ]
print(type(object))                 # <class 'type'>

# - instnace 생성
o1 = object()
print(type(o1))                     # <class 'object'>

# [ 'object' 상속 ]
class Person:
    pass

p1 = Person()

print(issubclass(Person, object))   # True
print(isinstance(p1, object))       # True


# [ Class 뿐만아니라 Function, Module 도 .. ]
def my_func():
    pass

print(isinstance(my_func, object))  # True


