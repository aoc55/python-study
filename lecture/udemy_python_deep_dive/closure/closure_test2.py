# [ Closure VS Class - #1 ]
# - 가장 비효율적인 방법
# - 매번 계산 필요

# < Class Ver >
class Averager:

    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        return sum(self.numbers) / len(self.numbers)


avg = Averager()
print(avg.add(10))
print(avg.add(10))
print("------------")


# < Closure Ver >
def averager():
    numbers = []

    def add(number):
        numbers.append(number)
        return sum(numbers) / len(numbers)

    return add


a = averager()
print(a(10))
print(a(15))
print(a(20))


print("------------")


# [ Closure VS Class - #2 ]
# - 내부 계산 로직 효율 향상

# < Class Ver >
class Averager2:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add(self, number):
        self.total += number
        self.count += 1
        return self.total / self.count


avg = Averager2()
print(avg.add(10))
print(avg.add(10))
print("------------")


# < Closure Ver >
def average2():
    total = 0
    count = 0

    def add(number):
        nonlocal total
        nonlocal count
        total += number
        count += 1
        return total / count

    return add


a2 = average2()
print(a2(3))
print(a2(3))
print(a2(4))


# [ Closure 실습 ]
def timer():

    from time import perf_counter
    start = perf_counter()

    def poll():
        return perf_counter() - start

    return poll


t = timer()
print(t())
print(t())


# [ Closure 실습 2 ]
def counter(initial=0):
    def inc(step=1):
        nonlocal initial
        initial += step
        return initial
    return inc


c = counter(100)
print(c(step=50))


# [ Closure 실습 3 ]
def counter_func(fn, count_dict):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        count_dict[fn.__name__] = count
        result = fn(*args, **kwargs)
        return result

    return inner


def print_hi():
    print('HI ~')


c = {}
print_hi = counter_func(print_hi, c)
print_hi()
print_hi()
print(c)


# Closure -> Basically Original Function 기능 + Extra
