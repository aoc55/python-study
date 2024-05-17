# [ Iterable with Generator ]
# - Generator 는 Exhausted 되기때문에 재사용불가
# - 이에 대한 해결책으로 iterable 한 객체를 별도로 만들고, __iter__ 에서 generator function 활용

def squares(n):                  # Generator Function
    for i in range(n):
        yield i ** 2


# - 재사용 불가
gener = squares(3)
print(list(gener))
print(list(gener), " -> Empty !!")


class Squares:                  # Iterable 한 객체 만들기
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return squares(self.n)


square = Squares(3)
print(list(square))
print(list(square), " -> 재사용 가능!")


