# [ Decorator 중첩하기 ]
def deco_1_before(fn):

    def inner(*args, **kwargs):
        print('<< Decorator_1_Before >>')
        result = fn(*args, **kwargs)
        return result

    return inner


def deco_2_before(fn):
    def inner(*args, **kwargs):
        print('<< Decorator_2_Before >>')
        result = fn(*args, **kwargs)
        return result

    return inner


def my_func_0():
    print("my_func_1")


my_func_0 = deco_1_before(deco_2_before(my_func_0))
my_func_0()

# 출력 결과
# << Decorator_1_Before >>
# << Decorator_2_Before >>
# my_func_1


@deco_1_before
@deco_2_before
def my_func_1():
    print("my_func_1")


my_func_1()

# 출력 결과
# << Decorator_1_Before >>
# << Decorator_2_Before >>
# my_func


# [ Decorator 중복사용 ]
@deco_1_before
@deco_1_before
@deco_1_before
def my_func_3():
    print("my_func_3")


my_func_3()
# 출력 결과
# << Decorator_1_Before >>
# << Decorator_1_Before >>
# << Decorator_1_Before >>
# my_func_3

