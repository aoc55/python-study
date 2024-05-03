# [ Type Annotation ]
# - python 3.6 ~ 이후에 도입

def my_func(a: str, b: str) -> str:
    return a + b


result = my_func('a', 'b')
print(result)


# - 그러나 강제성은 없음
# - IDE 에서 경고정도 ..
result2 = my_func(3, 10)
print(result2)


# [ Type Annotation 2]
# - 변수
my_var: int = 10

# - 역시 강제성은 없다
my_var = 'abcd'
print(my_var)

