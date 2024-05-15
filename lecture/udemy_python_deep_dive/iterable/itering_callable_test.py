# [ iter() 활용해서 callable Iterator 만들기 ]
# - iter(callable, sentinel) 활용
# - callable 은 여기서 메서드, 함수 등 ...

print(help(iter))
# iter(...)
#   iter(iterable) -> iterator
#   iter(callable, sentinel) -> iterator
print("-----------------")


# [ iter() 활용한 -> callables's iterator 생성 예시 1 ]
import random
random.seed(1)
random_iter = iter(lambda: random.randint(0, 10), 7)
for v in random_iter:
    print(v)

print("-----------------")


# [ iter() 활용한 -> callables's iterator 생성 예시 2 ]
def count_down(start=10):
    def run():
        nonlocal start
        start -= 1
        return start
    return run

takeoff = count_down(10)
takeoff_iter = iter(takeoff, -1)
for v in takeoff_iter:
    print(v)


print("-----------------")

# [ 직접 Callable's Iterator 만들어보기 ]

# - Callable 정의
def counter():
    i = 0
    def inc():
        nonlocal i
        i += 1
        return i
    return inc

# - 직접 Callable's Iterator 정의
# - 즉 아래와 같은 맥락의 Iterator 를 Python 이 만들어준다!
class CounterIterator:
    def __init__(self, counter_callable, sentinel):
        self.counter_callable = counter_callable
        self.sentinel = sentinel
        self.is_consumed = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_consumed:    # Iterator 소모된 후에 재 사용을 막기 위함
            raise StopIteration
        else:
            result = self.counter_callable()
            if result == self.sentinel:
                self.is_consumed = True
                raise StopIteration
            else:
                return result


# - 사용
counter = counter()
custom_iter = CounterIterator(counter, 5)
for v in custom_iter:
    print(v)

print("-----------------")
# - 소모 이후에 재사용 불가
try:
    next(custom_iter)
except StopIteration:
    print("StopIteration")


