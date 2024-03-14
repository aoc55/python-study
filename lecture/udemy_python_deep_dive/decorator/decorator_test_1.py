# [ Closure 복습  + Decorator 개념 ]
def counter(fn):                    # (1) 어떤 함수던
    """~ closure's counter docString ~"""
    count = 0

    def inner(*args, **kwargs):     # (2) 어떤 변수던
        """~ closure's inner docString ~"""
        nonlocal count
        count += 1
        print(f'-- Function {fn.__name__} called {count} times -- ')
        return fn(*args, **kwargs)
    return inner


def test():
    print("hi")


f = counter(test)
f()
f()

# - 기존 'test' 함수에 대해 'Wrapping' 처리 함 w 어떠한 기능 추가
# - 이럴때 위 예시의 'counter'를 decorator function 이라고 함


# [ Decorator Symbol ' @ ' ]
# - <Decorator 호출 패턴>
test = counter(test)
test()

# - <일반화>
# - my_func = decorate_func(my_func) -> my_func() 호출


# - <@ Symlbol 사용하기 >
@counter
def test2(a, b):
    return a + b


print(test2(1, 3))

# - <@ Symbol 사용 일반화>
# - @decorate_func
# - def my_func(....)


# [ Decoreated Function Introspect 1 ]
@counter
def test3(a, b):
    return a * b


print(test3.__name__)       # 결과 'inner' ! = 'test3'
help(test3)
# - closure의 'inner' 에 대한 docString, Function Signature 출력됨


# [ Decoreated Function Introspect 2 ]
# - Closure 로 입력받는 fn 함수의 instropect (docstring, .. )그대로 출력하게 하기
# - @wraps 사용
# - 필수는 아니지만 ...
from functools import wraps
def counter_V2(fn):
    """~ closure's counter docString ~"""
    count = 0

    @wraps(fn)  # 추가
    def inner(*args, **kwargs):
        """~ closure's inner docString ~"""
        nonlocal count
        count += 1
        print(f'-- Function {fn.__name__} called {count} times -- ')
        return fn(*args, **kwargs)
    return inner


@counter_V2
def test4(a, b):
    """ test4's docString"""
    return a * b

print(test4.__name__)
help(test4)                 # -> test 4의 docString 출력됨


