# [ Genenarotr Basic 1 ]
def song():  # song 은 Generator 를 생성하는 Generator Function
    print("line1")
    yield "return yield value1"
    print("line2")
    yield "return yield value2"


print(type(song()))     # <class 'generator'>

# - Generator 활용
my_gener = song()       # Generoatr 획득
print(next(my_gener))   # Generaotr 사용
print(next(my_gener))
try:
    print(next(my_gener))   # 모두 소모 되었는데 이후 호출 시
except StopIteration:
    print("StopIteration")

print("------------------")


# [ Genenarotr Basic 2 ]
# - NO Generatrver -> 직접 Iterator 구현 Ver
class FactIterOld:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            import math
            result = math.factorial(self.i)
            self.i += 1
            return result


# - Generater Ver
def factorials(n):
    import math
    for i in range(n):
        yield math.factorial(i)


fact_iter = factorials(3)   # -> generator function 으로 genertor 생성
print(type(fact_iter))      # -> <class 'generator'>
print(list(fact_iter))


print("------------------")


# [ Generator is Iterator ]
# - Generator 는 Iterator 의 한 종류
# - 따라서 Exhausted 될 수 있음
def my_generate_function(n):
    for i in range(n):
        yield i * 2


my_gener = my_generate_function(5)
print("최초 사용 = ", list(my_gener), " -> generator Exhausted")
print("이후 재사용? = ", list(my_gener), " -> Empty List")

print("------------------")


# [ Generator with 'Return' ]
def my_generate_function2():
    yield 1
    yield 2
    if True:
        return False # Return 구문 만날 경우 StopIteration Raise!!
    yield 3


my_gener = my_generate_function2()
print(next(my_gener))
print(next(my_gener))
try:
    print(next(my_gener))
except StopIteration:
    print("StopIteration")

