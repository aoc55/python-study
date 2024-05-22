# [ Count 실습 ]
# - 'Lazy' Iterator
# - range와 유사하나, range 는 정수만 가능하고, finite 함
# - 반면 Count 는 infinite 하고 실수, 복소수 등 가능
# - 'infinite' 하기때문에 islice 와 함께 쓰임..
from itertools import count, islice

print(list(islice(count(10, 2), 5)))        # [10, 12, 14, 16, 18]

print(list(islice(count(0.1, 0.1), 3)))     #  [0.1, 0.2, 0.30000000000000004]

# [ Cycle 실습 ]
# - 'Lazy' Iterator
# - parameter 로 전달된 (finite 한) iterable 을 infinite 하게 실행

from itertools import cycle
my_list = ['a', 'b', 'c']
print(list(islice(cycle(my_list), 4)))      # ['a', 'b', 'c', 'a']

# - 중요점으로 argument 로 iterator 로 전달 시, exhausted 된 이후에도 계속 사용됨
my_generator = (x for x in range(3))
print(list(islice(cycle(my_generator), 6)))     # [0, 1, 2, 0, 1, 2]

# [ Repeat 실습 ]
# - 'Lazy' Iterator
# - '똑같은 Value'에 대해 무한대로 repeat
from itertools import repeat
print(list(islice(repeat('test'), 3)))          # ['test', 'test', 'test']

# - 주의점으로 리턴되는 object 들의 메모리는 모두 동일하다 (동일한 객체)
data = list(islice(repeat('a'), 3))
print(id(data[0]), id(data[1]), id(data[2]))    # 4378749488 4378749488 4378749488




