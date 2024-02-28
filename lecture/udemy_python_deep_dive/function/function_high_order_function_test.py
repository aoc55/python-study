# [ Map ]
def my_func1(x):
    return x * 2


map_result1 = map(my_func1, [1, 2, 3])
print(type(map_result1))

result1 = list(map_result1)     # 최초 소모
print(result1)                  # [2, 4, 6]

result1_2 = list(map_result1)   # 한번 소모된 이후로 재사용 불가
print(result1_2)                # []


# [ Map with Lambda ]
map_result2 = map(lambda x: x * 3, [1, 2, 3])
print(list(map_result2))


# [ Map with Multi Iterables ]
print(list(map(lambda x, y: x + y, [1, 2, 3], [10, 20, 30])))


# [ Filter ]
filter_result1 = filter(lambda x: x % 2 == 0, range(10))
print(type(filter_result1))     # <class 'filter'>
print(list(filter_result1))     # [0, 2, 4, 6, 8]
print(list(filter_result1))     # [] -> 역시 소모된 이후로 재사용 불가

# [ Fitler 2 ]
# - argument 의 Func 를 None 으로 할 경우
print(list(filter(None, [0, 1, True, False, 777, None])))       # [1, True, 777]


# [ Zip ]
print(list(zip([1, 2, 3], ['가', '나', '다'])))                # [(1, '가'), (2, '나'), (3, '다')]
print(list(zip([1, 2, 3, 4, 5, 6], ['가', '나', '다'])))       # [(1, '가'), (2, '나'), (3, '다')]
print(list(zip(range(1, 100), ['가', '나', '다'])))            # [(1, '가'), (2, '나'), (3, '다')]


# [ List Comprehension ]
# - List Comprehension을 통한 Map 대체
print(list(map(lambda x: x*2, [1, 2, 3])))
print([x * 2 for x in [1, 2, 3]])

print(list(map(lambda x, y: x+y, [1, 2, 3], [10, 20, 30])))
print([x + y for x, y in zip([1, 2, 3], [10, 20, 30])])


# [ List Comprehension 2 ]
# - List Comprehension을 통한 Filter 대체
l = [1, 2, 3, 4]
print(list(filter(lambda n: n % 2 == 0, l)))
print([x for x in l if x % 2 == 0])


# [ List Comprehension 3 ]
# - List Comprehension을 통한 Map & Filter 대체
l = range(10)
print(list(filter(lambda y: y < 25, map(lambda x: x**2, l))))
print([x ** 2 for x in l if x ** 2 < 25])


# [ Reduce 컨셉 ]

l = [5, 8, 6, 10, 9]
max_value_func = lambda a, b: a if a > b else b


# - Reduce 미사용 시 (직접구현)
def max_of_sequence(seq):
    result = seq[0]
    for e in seq[1:]:
        result = max_value_func(result, e)
    return result


print(max_of_sequence(l))


# - Reduce 컨셉 구현
# - (물론 실제는 Sequence 뿐만 아니라 Iterable 가능한 모든 타입에 대해 Reduce 가능)
def _reduce(fn, seq):
    result = seq[0]
    for e in seq[1:]:
        result = fn(result, e)
    return result


print(_reduce(max_value_func, l))
print(_reduce(lambda x, y: x if x < y else y, l))       # min 으로 응용
print(_reduce(lambda x, y: x+y, l))                     # sum 으로 응용


# [ Reduce 사용 ]
# - Any Iterable 에 대해 적용 가능
from functools import reduce
print(reduce(lambda a, b: a if a > b else b, l))
print(reduce(lambda a, b: a if a < b else b, l))
print(reduce(lambda a, b: a+b, l))
print(reduce(lambda a, b: a + '.' + b, 'abcde'))    # print('.'.join('abcde'))


# [ "Built-In" Reducing Function ]
# - Python 에 Built-In 된 Reduce Function 류
l = [5, 8, 6, 10, 9]
print(min(l))
print(max(l))
print(sum(l))

l_t = (True, True, True)
print(any(l_t))                 # True
print(all(l_t))                 # True

l_f_t = (True, False, True)
print(any(l_f_t))               # True
print(all(l_f_t))               # False


# [ Reduce 구현 예시 1 ]
# - Iterable 내 모든 요소 곱하기
print(reduce(lambda x, y: x*y, (1, 2, 3)))


# [ Reduce 구현 예시 2 ]
# - Factorial 구현하기
def my_factorial(n):
    return reduce(
        lambda before, now: before * now,
        range(1, n + 1))


print(my_factorial(5))


# [ Reduce with 초기값 ]
# - 초기값 지정 시 초기값 부터 Reduce 시작
empty_l = []
print(reduce(lambda x, y: x * y, empty_l, [999]))       # [999]

print(reduce(lambda x, y: x + y, [1, 2, 3], 1000))      # 1006


# [ Partial 컨셉 ]
# - 파라미터 줄이기
def my_func(a, b, c):
    print(f'a={a}, b={b}, c={c}')


# - Proxy 처럼 래핑
def fn1(b, c):
    return my_func('999', b, c)


# - 혹은 람다 활용
fn2 = lambda b, c: my_func('999', b, c)


# [ Partial 사용 ]
from functools import partial
f = partial(my_func, 1)
f(2, 3)


# [ Partial 사용 2 ]
def my_complex_func(a, b, *args, k1, k2, **kwargs):
    print("----")
    print(a, b, args, k1, k2, kwargs, sep='\n')
    print("----")


f = partial(my_complex_func, 'a', k1='k1')
f('b', k2='k2')
f('b', 'add1', 'add2', k2='k2', kadd1='kadd1', kadd2='kadd2')


f2 = partial(my_complex_func, b='b')
f2('a', k1='k1', k2='k2', kadd1='kadd1', kadd2='kadd2')

# - partial 에 지정해도 Override 가능
f2('a', b='override b', k1='k1', k2='k2', kadd1='kadd1', kadd2='kadd2')


# [ Partial 사용시 주의사항 ]
def my_func_easy(a, b):
    print(a, b)

sample_a = 999
f3 = partial(my_func_easy, sample_a)
f3('b')         # 999 b

# - partial 정의 시 사용했던 변수 변경
# - 그래도 변경되지 않음!
sample_a = 1000
f3('b')        # 999 b  -> 변경되지 않음

# [ Partial 사용시 주의사항 ]
def my_func_easy(a, b):
    print(a, b)

sample_a = 999
f3 = partial(my_func_easy, sample_a)
f3('b')         # 999 b

# - partial 정의 시 사용했던 변수 변경
# - 그래도 변경되지 않음!
sample_a = 1000
f3('b')        # 999 b  -> 변경되지 않음

