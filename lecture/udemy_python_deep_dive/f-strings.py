# [ 기존 방식 ]
# - "~~~ {} ~~ ".format() 방식 사용
my_str = "{} % {} = {}".format(10, 3, 10 % 3)
print(my_str)

my_str2 = "{1} % {2} = {0}".format(10 % 3, 10, 3)
print(my_str2)


# [ f-String 활용 ]
# - python 3.6 ~
# - 변수 조회, Expression 사용 등
a = 10
b = 3
my_str3 = f'{a} % {b} = {a % b}'        # 변수 조회 뿐만 아니라 Expression 도 가능
print(my_str3)


# [ f-String 활용 2 ]
# - 출력형식 지정하기
# - ex. :0.5f
print(f'test = {10 / 3: 0.5f}')         # 소숫점 등 출력형식 지정하기


# [ f-String 활용 3 ]
# - 해당 namespace 외 변수에 대해서도 당연히 사용 가능
def outer():
    name = 'Python'
    def inner():
        # nonlocal name
        return f'{name} Rocks!'
    return inner


my_func = outer()
print(my_func())


# [ f-String 활용 4 ]
# - lambda 구문도 호출 가능
my_labmda = lambda x: x**2

a = 10
b = 3

print(f'{my_labmda(a) > my_labmda(b)}')

