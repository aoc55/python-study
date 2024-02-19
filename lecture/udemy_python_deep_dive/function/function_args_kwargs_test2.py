

# [ *args + **kwargs ]
# - 가장 유연한 Argument 구조
def func(*args, **kwargs):
    print(f'args={args}, kwargs={kwargs}')


func(1, 2, 3, a='a', b='b', c='c')


# [ Keyword Only Argument 1]
def func1(*args, a, b):         # a, b -> Keywork Only Argument
    print(f'args={args}, a={a}, b={b}')


func1('1', '2', '3', a=10, b=20)


# [ Keyword Only Argument 2]
# - Keyword Only 강제하기
def func2(*, a, b):
    print(f'a={a}, b={b}')


# func2('a', 'b') 불가
func2(a='a', b='b')


# [ 복합 ]
def func3(a, b, c=10, *args, kw1, kw2=100, **kwargs):
    print("----")
    print(f'a={a}, b={b}, c={c}')
    print(f'args={args}')
    print(f'kw1={kw1}, kw2={kw2}')
    print(f'kwargs={kwargs}')
    print("----")


func3(1, 2, 3, 4, 5, 6, kw1='k1', kw2='k2', kw3='a', kw4='b')\

# 기본 값 있는 경우 생략
# - 단, *args가 있는 한 -> C 생략 불가함
func3(1, 2, 4, 5, 6, kw1='k1', kw3='a', kw4='b')


# *args, **kwargs 생략 + 기본 값 있는 경우 생략
func3(1, 2, kw1='k1')


# [ Use Case Sample ]
# - log_to_console => Keyword 'Only' Argument
def calc_hi_lo_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)
    lo = int(bool(args)) and min(args)
    avg = (hi + lo) / 2
    if log_to_console:
        print("high={0}, low={1}, avg={2}".format(hi, lo, avg))
    return avg


calc_hi_lo_avg(10, 20, 30)
calc_hi_lo_avg(10, 20, 30, log_to_console=True)
