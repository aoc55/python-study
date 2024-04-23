from ..decorator.decorator_test_2 import timed_final

# [ 피보나치 구현 # 1]
# - 재귀 방식
def fibonacci_recur(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recur(n-1) + fibonacci_recur(n-2)


def call_fibonacci_recur(n):
    print(fibonacci_recur(n))


call_fibonacci_recur(3)

#