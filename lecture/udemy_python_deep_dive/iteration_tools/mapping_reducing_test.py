# [ Mapping -> Map 실습 ]
# - map 에서 fn 은 'Single' Argument 로 동작하는 함수
import itertools

map_result = map(lambda x: x**2, range(5))

# - map 결과가 (Lazy) Iterator 임을 확인
print(iter(map_result) is map_result)       # True
print('__next__' in dir(map_result))        # True

# - map 결과 출력
print('By Map:', list(map_result))                     # 물론 이때 Exhausted 됨

# - 물론 Generator Expression 으로 동일하게 가능
fn = lambda x: x ** 2
print('By G.E', list((fn(i) for i in range(5))))

print("----------------------------------------")

# [ Mapping -> starmap 실습 ]
# - map 과 유사하나, 'Multi-Argument Function' 을 인자로 받음
from itertools import starmap
multi_fn = lambda x, y, z: x + y + z
target_data = [(1, 1, 1), (2, 2, 2), (3, 3, 3)]

try:
    print(list(map(multi_fn, target_data)))
except TypeError:
    print("Type Error -> Map 의 fn 은 single Arguemnt fn 만 가능!!")

print('By starmap:', list(starmap(multi_fn, target_data)))


# - starmap 활용예제2
data = [[1, 2], [3, 4]]
import operator
print(list(starmap(operator.mul, data)))

# - G.E 로 동일하게 구현?
print('By G.E : ', list((operator.mul(*item) for item in data)))

print("----------------------------------------")

# [ Accumulate -> reduce 실습 ]
from functools import reduce

# - reduce 의 결과는 Single Value
data = [1, 2, 3, 4]
print('Reduce Reuslt:', reduce(lambda x, y: x + y, data))
print('Reduce with Init Value :', reduce(lambda x, y: x + y, data, 10000))


print("----------------------------------------")

# [ Accumulate -> iterator 실습 ]
# - lazy iterator 임
# - reduce 와 argument 위치가 반대
# - reduce 는 'only final result' 만 반환 vs 'accumualte'는 중간 값까지 iterator 로 반환
from itertools import accumulate
data = [1, 2, 3, 4]

print(list(itertools.accumulate(data)))                 # fn 미지정하면 add 가 기본
print(list(itertools.accumulate(data, operator.mul)))


# - 활용예시 두개의 iterable 합쳐서 누적하기 (with chain)
from itertools import chain
print(list(accumulate(chain([1, 2, 3], [4, 5, 6]), operator.mul)))


# [ Accumulate -> 직접 구현 ]
# - 단순 참고만!
# - reduce? accumulate 직접구현
def sum_(iterable):
    it = iter(iterable)     # 첫번째 리턴을 위함
    acc = next(it)
    yield acc
    for item in it:         # 이후 누적해서 리턴
        acc += item
        yield acc


print(sum_([1, 2, 3, 4]))


def running_reduce(fn, iterable, start=None):
    it = iter(iterable)
    acc = start if start is not None else next(it)
    yield acc
    for item in it:
        acc = fn(acc, item)
        yield acc


print(list(running_reduce(lambda x, y: x+y, [1, 2, 3, 4])))
print(list(running_reduce(operator.add, [1, 2, 3, 4])))
print(list(running_reduce(operator.mul, [1, 2, 3, 4])))


print("----------------------------------------")
