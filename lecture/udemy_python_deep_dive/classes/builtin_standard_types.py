# [ Built-in Types ]
l = [1, 2, 3]
i = 1
mystr = 'hi'

print(type(l) is list)
print(type(i) is int)
print(type(mystr) is str)


# [ Standard Types ]
# - 'types' 모듈 통해서 체크 가능
import types


def my_func():
    pass


def my_gen():
    for i in range(10):
        yield i


print(type(my_func) is types.FunctionType)
print(type(my_gen) is types.GeneratorType)
