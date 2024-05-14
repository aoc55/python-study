# [ Iterator Protocol 구현 ]
class Squares:
    def __init__(self, length):
        self.length = length
        self.i = 0

    def __len__(self):
        return self.length

    def __next__(self):
        print('>> python called __next__')
        if self.i >= self.length:
            print('>> raise StopIteration!!')
            raise StopIteration

        result = self.i ** 2
        self.i += 1
        return result

    def __iter__(self):
        print('>> python called __iter__')
        return self


# - 이제 for 구문 구현 가능
sq = Squares(5)
for item in sq:
    print(item)
print("-----------------")

# - 그러나 Exhausted 되버려서 처음부터 Iter 다시 시작 등 불가
try:
    next(sq)
except StopIteration:
    print("StopIteration", "Exhausted")


# [ Iterator Protocol 구현2 ]
# - Iterator Protocol 구현에 따라, iterable 를 인자로 받는 곳에 사용 가능해짐
print("-----------------")
sq = Squares(5)
sorted_sq = sorted(sq, reverse=True)
print(sorted_sq)


# [ Python for 구문 호출 방식 ]
sq = Squares(5)
sq_iterator = iter(sq)
while True:
    try:
        item = next(sq_iterator)
        print(item)
    except StopIteration:
        break

# - 파이썬의 for-구문은 실제로 위와 같은 방식으로 동작됨
