import random


# [ Custom 한 iterable 객체 만들어보기 1 ]
class Squares:
    def __init__(self):
        self.i = 0

    # Cusotmizing Next
    def next_(self):
        result = self.i ** 2
        self.i += 1
        return result


sq = Squares()
print(sq.next_())
print(sq.next_())
print(sq.next_())
print(sq.next_())


# - 그러나 .. 문제점 !
# - 다시 시작(Restart) 등 불가
# - 정지가 없음 -> 무한대로?
# - 위 클래스를 통해서 for loop, comprehension 등 불가



# [ Custom 한 iterable 객체 만들어보기 - 2]
# - infinite -> 개선
print("-----------------")
class Squares:
    def __init__(self, length):
        self.length = length
        self.i = 0

    def __len__(self):
        return self.length

    # Cusotmizing Next
    def next_(self):
        if self.i >= self.length:
            raise StopIteration

        result = self.i ** 2
        self.i += 1
        return result



sq = Squares(3)
print(sq.next_())
print(sq.next_())
print(sq.next_())
try:
    print(sq.next_())
except StopIteration:
    print("StopIteration")



print("-----------------")
sq = Squares(5)
while True:
    try:
        print(sq.next_())
    except StopIteration:
        break


# [ Custom 한 iterable 객체 만들어보기 - 3]
# - python 의 next 활용
print("-----------------")
class Squares:
    def __init__(self, length):
        self.length = length
        self.i = 0

    def __len__(self):
        return self.length

    def __next__(self):
        if self.i >= self.length:
            raise StopIteration

        result = self.i ** 2
        self.i += 1
        return result


sq = Squares(5)
while True:
    try:
        # print(sq.__next__())
        print(next(sq))
    except StopIteration:
        break


print("-----------------")
# 하지만 여전히 for 문 통한 접근은 안됨
try:
    sq = Squares(10)
    for item in sq:
        print(sq)
except TypeError:
    print("TypeError")


# [ Custom 한 iterable 객체 만들어보기 - 3]
# - 예시
print("-----------------")
class RandomNumbers:
    def __init__(self, length, *, range_min=0, range_max=10):
        self.length = length
        self.range_min = range_min
        self.range_max = range_max
        self.num_requested = 0

    def __len__(self):
        return self.length

    def __next__(self):
        if self.num_requested >= self.length:
            raise StopIteration
        else:
            self.num_requested += 1
            return random.randint(self.range_min, self.range_max)

numbers = RandomNumbers(3)
while True:
    try:
        print(next(numbers))
    except StopIteration:
        print("StopIteration")
        break

print("-----------------")
# - 하지만 여전히 for 문 통한 접근은 안됨!!!
try:
    rn = RandomNumbers(10)
    for item in rn:
        print(rn)
except TypeError:
    print("TypeError")

# - 또한 동일한 instance 로 Restart from the beginning 등 불가
# - iterator_test 에서 이어서 진행