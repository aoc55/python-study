from functools import singledispatch

@singledispatch
def base_function(arg):
    print("hi this is base function = ", arg)


@base_function.register(int)
def _int(arg):
    print("hi this is int = ", arg)


@base_function.register(str)
def _int(arg):
    print("hi this is string = ", arg)


if __name__ == '__main__':

    base_function(10)
    base_function('STR')
    base_function(10.77)        # double 지정 안함 -> base 수행