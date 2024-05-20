# [ Filter 실습 ]
# - 결과가 True 인 Element 만 추출
# - filter(predicate, iterable)
def get_cubes(n):
    for i in range(n):
        print(f'<Yielding> {i}')
        yield i ** 3


is_odd = lambda x: x % 2 == 1

filtered = filter(is_odd, get_cubes(5))
print(filtered)                             # <filter object at 0x100a28550> -> LAZY Iterator
print(list(filtered))                       # [1, 27]


filtered2 = filter(None, get_cubes(5))      # Predciate -> None 으로 할 경우 Identity Function
print(list(filtered2))                      # [1, 8, 27, 64]

print("------------------------------------------")

# [ Filterfalse 실습 ]
# - 결과가 False 인 Element 만 추출
from itertools import filterfalse
filtered3 = filterfalse(is_odd, get_cubes(5))
print(list(filtered3))                      # [0, 8, 64]


print("------------------------------------------")

# [ dropwhile 실습 ]
# 조건이 만족하지 '않을때까지' 계속 'Drop' !!
from itertools import dropwhile
data = [1, 3, 5, 2, 1]
print(list(dropwhile(lambda x: x < 5, data)))      # [5, 2, 1]

print("------------------------------------------")


# [ takewhile 실습 ]
# 조건이 만족하지 '않을때까지' 계속 'Take' !!
from itertools import takewhile
data = [1, 3, 5, 2, 1]
print(list(takewhile(lambda x: x < 5, data)))       # [1, 3]

print("------------------------------------------")

# [ compress 실습 ]
# - 실제 유용하게 쓰일 수 있음 !!
from itertools import compress
data = list('abcde')
selectors = [True, False, 1, 0, None]
print(list(compress(data, selectors)))      # ['a', 'c']