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