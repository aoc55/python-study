# [ * : Unpacking Operator ]
my_list = [1, 2, 3, 4, 5]
(*a,) = my_list
print(f'a={a}, type={type(a)}')             # * 결과는 "List"


# [ *args - 1]
def my_func1(a, b, *c):
    print(a, b, c)
    print(f'c={c}, type={type(c)}')         # *args 결과는 "Tuple" 임


my_func1(1, 2, 3, 4, 5)


# [ *args - 2]
# - *args 이후에 선언된 파라미터는 Keyword Argument 필수로 사용해야함
def my_func2(a, b, *args, d):       # d 는 필수로 Keyword Argument 로 사용
    pass


my_func2(1, 2, 3, 4, 5, d=777)


# [ *args - 3]
# - Unpacking Operator 활용한 파라미터
def my_func3(a, b, c):
    print(f'a={a}, b={b}, c={c}')


my_list3 = [1, 2, 3]
# my_func3(my_list3)   -> 불가
my_func3(*my_list3)    # Unpacking 해서는 가능
my_func3(*"abc")


# [ *args - 4]
# - 실습
def my_avg(*args):
    count = len(args)
    total = sum(args)
    # 'count and' args {} 일 경우 대비한 로직
    return count and total / count


print(my_avg(1, 2, 3))
print(my_avg())


# [ *args - 4]
# - 실습2
def my_avg2(a, *args):      # 반드시 값 하나는 입력하도록 하기
    count = len(args) + 1
    total = sum(args) + a
    return count and total / count


print(my_avg2(1, 2, 3))
# print(my_avg2()) 불가능


# [ Keyword Argument 1]
# - with *args
def my_func4(*args, d):     # d 필수로 keyword Argument 로 사용 필요
    print(f'd={d}')


my_func4(1, 2, 3, d='필수')
my_func4(d='필수')


def my_func5(*args, d='기본값'):     # 단, 기본 값 있으면 생략 가능
    print(f'd={d}')


my_func5(1, 2, 3)


# [ Keyword Argument 2]
# with NO Positional Arguments
def my_func6(*, d):         # *로 사용한 경우 Poistional Argument X
    print(f'd={d}')


# my_func6(1, d='hi') 불가
my_func6(d='hi')


# [ Keyword Argument 3]
# - 복합 실습
def my_func7(a, b=1, *args, d, e=True):
    pass


my_func7('a', 'b', 1, 2, 3, d='d', e='e')       # 모두 사용
my_func7('a', 'b', 1, 2, 3, d='d')              # - e 기본 값 있으므로 생략 (d는 불가능)
my_func7('a', 1, 2, 3, d='d')                   # - b 기본 값 있으므로 생략
my_func7('a', d='d')                            # - *args 생략


# [ **kwargs 1]
# - 결과 반환 값은 dict
def my_func8(p, **kwargs):
    print(f'p={p}, kwargs={kwargs}')


my_func8(1, a='a', b='b', c='c')


def my_func9(**kwargs):
    print(f'kwargs={kwargs}')


my_func9(a='a', b='b', c='c')
my_func9()     # empty dict

# [ **kwargs 2]
# - **kwargs 뒤로 Paramater 올 수 없음!!
# def my_func10(p, **kwargs, q):    q 불가!


# [ *args, **kwargs ]
def my_func11(*args, **kwargs):
    print(f'args={args} type={type(args)}')
    print(f'kwargs={kwargs} type={type(kwargs)}')


my_func11(1, 2, 3, 4, a='a', b='b', c='c')
