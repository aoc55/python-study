# [ Default Value ]
def my_func(a, b=20, c=30):
    print(f'{a}, {b}, {c}')

# 아래와 같이, 중간에 Default Value 설정 불가
# def my_func(a, b=10, c): *불가!*


my_func(10, 20)
my_func(10)
my_func(10, c=50)       # b는 default Value 사용, c는 대입하고 싶을 경우 -> keyword Argument 사용


# [ Keywork Argument ]
my_func(10, b=200, c=300)
# my_func(a:10, b=200, 300) *불가!* -> Keyword Name 사용 시 이후 변수들도 Keyworkd name 사용 필요
my_func(10, b=200)      # 단, default Value 설정 시 생략 가능
my_func(c=300, b=200, a=100)
my_func(100, c=300, b=200)


