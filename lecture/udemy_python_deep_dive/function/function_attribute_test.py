def my_func(a, b):
    return a + b


# [ Function 에 Custom Attribute 부여하기 ]
my_func.category = 'math'
my_func.sub_category = 'arithmetic'

print(my_func.category)
print(my_func.sub_category)

# [ Function 의 전체 Attirbute 출력하기 ]
print(dir(my_func))


# [ Function 주요 Attribute 1 ]
def my_func2(a, b=2, c=3, *, kw1, kw2=2):
    pass


print(my_func2.__name__)                # my_func2
print(my_func2.__defaults__)            # (2, 3)
print(my_func2.__kwdefaults__)          # {'kw2': 2}


# [ Function 주요 Attribute 2 ]
def my_func3(a, b=1, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b


print(my_func3.__code__)                # <code object my_func3 at 0x1008695b0, ...
print(my_func3.__code__.co_varnames)    # ('a', 'b', 'args', 'kwargs', 'i') 내부 변수 i  포함
print(my_func3.__code__.co_argcount)    # Number of Parameter -> 2 (*args, **kwargs 제외)



