# [ 'List' Sequence Type 의 Iterator ]
my_list = [1, 2, 3, 4]
my_list_iter = iter(my_list)
print(type(my_list_iter))      # <class 'list_iterator'>
print(next(my_list_iter))
print(next(my_list_iter))
print(next(my_list_iter))
print("-----------------")


# [ __getitem__ 구현시 Iterator 자동생성됨]
class Squares:

    # __iter()__ 별도로 구현 안함

    def __init__(self, n):
        self._n = n

    def __len__(self):
        return self._n

    def __getitem__(self, i):
        if i >= self._n:
            raise IndexError
        else:
            return i ** 2


square = Squares(3)
square_iter = iter(square)      # 자동 생성된 iter 활용
print(next(square_iter))
print(next(square_iter))
print(next(square_iter))

for v in square:
    print(v, end=" ")

print()
print("-----------------")


# [ 자동 생성되는 iter() - 직접 구현해보기 ]
# - 즉, 아래와 같은 flow 로 iterator 객체가 자동생성
class CustomSeqIterator:
    def __init__(self, squares):
        self._squares = squares
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i >= len(self._squares):
            raise StopIteration
        else:
            result = self._squares[self._i]
            self._i += 1
            return result


square = Squares(3)
square_iter_custom = CustomSeqIterator(square)     # 직접 생성한 iter 활용
print(next(square_iter_custom))
print(next(square_iter_custom))
print(next(square_iter_custom))
print("-----------------")


# [ Iterable or Not -> 판별하기 ]
# - iter(x) 해보기?
# - 물론 실제로 사용하는일 은 잘 없을 듯...
def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


# - iter() 구현 안한 샘플
class NotIter:
    def __init__(self):
        pass

    def __iter__(self):
        return 'NOT IMPLEMENTED'


print(is_iterable(NotIter()))
