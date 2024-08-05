# [ Decorator Review ]
from functools import wraps

def debugger(fn):

    @wraps(fn)
    def inner_func(*args, **kwargs):
        print(f'{fn.__qualname__}', args, kwargs)
        return fn(*args, **kwargs)

    return inner_func

@debugger
def my_func(*args, **kwargs):
    pass

@debugger
def my_func2(*args, **kwargs):
    pass


my_func(1, 2, 3)
my_func2('a', 'b', k=10)



# [ Descriptor Review ]

class IntegerField:

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        print(" >>>> set called ", self.name, value)
        if not isinstance(value, int):
            raise TypeError("Must Be An Integer")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        print(" >>>> get called ", self.name)
        return instance.__dict__.get(self.name, None)

class Point:

    x = IntegerField()
    y = IntegerField()

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(10, 20)
print()

print(p.x, p.y)
