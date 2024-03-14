# [ Decorator Parameter ]
# - 데코레이터에 파라미터 ?

def timed(fn):
    from functools import wraps
    from time import perf_counter

    @wraps(fn)
    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(10):
            start = perf_counter()
            result = fn(*args, **kwargs)
            total_elapsed += (perf_counter() - start)
        avg_elapsed = total_elapsed / 10
        print(f'{fn.__name__} : 10번 수행 결과 -> {avg_elapsed}')
        return result
    return inner

@timed
def my_func(a, b):
    return a + b


print(my_func(10, 5))


# [ Decorator Parameter - 시도 ]
# - 데코레이터에 파라미터 ?
def timed_v2(fn, reps):
    from functools import wraps
    from time import perf_counter

    @wraps(fn)
    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(reps):                     # 하드코딩 10이 아닌 변수화
            start = perf_counter()
            result = fn(*args, **kwargs)
            total_elapsed += (perf_counter() - start)
        avg_elapsed = total_elapsed / reps
        print(f'{fn.__name__} : {reps} 수행 결과 -> {avg_elapsed}')
        return result
    return inner


# - <데코레이터 직접 호출 : 가능>
def my_func2_1(a, b):
    return a + b


my_func2_1 = timed_v2(my_func2_1, 10)
my_func2_1(10, 20)

# - <@ Symbol 사용 ? -> 불가>
# - @timed_v2(10)
# - def my_func2_1(a, b):
# -     return a + b


# [ Decorator Parameter - By Decorator Factory Function ]
# <사용목표 : @timed(10)>
# <Solution> 
#  @ 1단계. dec = @timed(10)    (dec 역시 데코레이터)
#  @ 2단계. @dec
#           def my_func(): ...
def outer(reps):                            # 1단계
    def timed_v3(fn):                       # 2단계
        from functools import wraps
        from time import perf_counter
    
        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / reps
            print(f'{fn.__name__} : {reps} 수행 결과 -> {avg_elapsed}')
            return result
        return inner
    return timed_v3


@outer(10)
def my_func3_1(a, b):
    return a + b


my_func3_1(1, 1)


def my_func3_2(a, b):
    return a + b


my_func3_2 = outer(10)(my_func3_2)
my_func3_2(1, 1)

# <Decorator Factory Function>
# - "outer" 자체는 Decorator X -> 대신 호출 시 Decorator 인"timed_v3" 반환
# - 어떤 Argument 던 "outer" 에 전달이 되면, 안에 있는 Decorator "timed_v3 가 참조할 수 있음
# - 즉, Decorator 가 참조할 수 있는 Argument 보관 역할?
# - 여기서 "outer" 함수를 Decorator Factory Function 이라고 함
# - 그리고 Decorator Factory Function 호출 시마다 새로운 Decorator 생성됨


# [ Decorator Parameter - Finall ]
# - Decorator Factory Function 사용해서 예시 구현
def timed_final(reps):

    def dec(fn):  # 2단계
        from functools import wraps
        from time import perf_counter

        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / reps
            print(f'{fn.__name__} : {reps} 수행 결과 -> {avg_elapsed}')
            return result

        return inner

    return dec


@timed_final(5)
def my_func_final(a, b):
    return a + b


my_func_final(10, 10)

