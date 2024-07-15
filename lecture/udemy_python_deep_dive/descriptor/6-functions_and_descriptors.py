# [ Function & Descriptor 실습 ]
def add(a, b):
    return a + b

# - Function 의 경우 Non-Data Descriptor Protocol 구현!
print(hasattr(add, '__get__'))          # True
print(hasattr(add, '__set__'))          # False

print("-------------------------")

# [ Method 객체 생성 (바인딩) ]
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f'{self.name} says Hello !!'

# - Function Object
print(Person.say_hello)
print("")

# - Method Object
p = Person('kgh')
print(p.say_hello)
print("")

# - Method Object 직접 만들기 with Descriptor
bound_method = Person.say_hello.__get__(p, Person)
print(type(bound_method), "--> ", bound_method)
print(bound_method.__func__)
print(bound_method())
