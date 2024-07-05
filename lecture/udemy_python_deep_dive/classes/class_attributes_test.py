# [ Callable Class Atribute ]
class Program:
    language = 'Python'

    def say_hello():        # Callable !!
        print(f'Hello From {Program.language}')


getattr(Program, 'say_hello')()     # Call
Program.say_hello()                 # Call
print(Program.__dict__)
# 'say_hello': <function Program.say_hello at 0x104b98040>

print('----------------------------')

# [ Class is Callable ]

p = Program()           # Class is Callable !

print(type(p))
print(isinstance(p, Program))

# 별도의 namespace 보유
print('p -> ', p.__dict__)
print('Program -> ', Program.__dict__)

print(p.__class__)
print(type(p) is p.__class__)

# type(..) or isinstance(..) 을 쓰는게 안전한 이유

class MyClass:
    __class__ = str         # 사실 이렇게 쓰는게 잘못되긴 함


m = MyClass()
print(m.__class__, type(m))

print('----------------------------')

# [ Data Attributes ]
class BankAccount:
    apr = 1.2                           # Class Atribute !!


acc_1 = BankAccount()
acc_2 = BankAccount()
print(acc_1 is acc_2)
print(acc_1.__dict__, acc_2.__dict__)

# From 'BackAccount' Namespace
print(acc_1.apr, acc_2.apr)

BankAccount.account_type = 'Savings'            # Class Attribute
print(BankAccount.account_type)
print(acc_1.account_type, acc_2.account_type)   # From Class Atribute

print("--acc_1-- 수정")
acc_1.apr = 0                           # Instance Attribute !!
print(acc_1.apr, acc_2.apr)
print(acc_1.__dict__, acc_2.__dict__)

print("--acc_2-- 수정")
setattr(acc_2, 'apr', 10)                # Instance Attribute !!
print(acc_1.apr, acc_2.apr)
print(acc_1.__dict__, acc_2.__dict__)

print('--default--')
print(getattr(BankAccount(), 'apr'))     # From Class Atribute

print("-----------------------------------------")

# [ Read-Only Properites ]
import math


class Circle:
    def __init__(self, r):
        self._r = r
        self._area = None

    @property
    def radius(self):
        return self._r

    @radius.setter
    def radius(self, r):
        if r < 0:
            raise ValueError("Must Be Non Negative")
        self._r = r
        self._area = None       # Invalidate Cache

    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * (self.radius ** 2)       # Set Cache
        return self._area


circle = Circle(3)
print(circle.__dict__)
print(circle.area)
print(circle.__dict__)
print("")

circle.radius = 2
print(circle.__dict__)
print(circle.area)
print(circle.__dict__)

print(circle._r) # 강제 접근은 가능

print("-----------------------------------------")

# [ Delete Properties ]

# - Old Style
class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def del_name(self):
        del self._name


p1 = Person("aaa")

p1.set_name("kgh")
print(p1.get_name())
print(p1.__dict__)

p1.del_name()
print(p1.__dict__)
print("")


# - New Style
class PersonV2:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # - deleter 구현
    @name.deleter
    def name(self):
        print('----> deleter ..')
        del self._name


p2 = PersonV2("aaa")
p2.name = 'kgh'
print(p2.name)
print(p2.__dict__)

del p2.name
print(p2.__dict__)
