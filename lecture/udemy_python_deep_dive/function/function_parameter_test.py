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


# [ Default Value 주의사항 1 ]
# - 모듈이 Loaded 될때 모든 코드는 실행됨
# - 함수의 경우 def ~ 정의 구문이 실행됨
# - 따라서 argument 에 defalut Value 설정 시 주의해야함
from datetime import datetime


def my_log(msg, *, dt=datetime.now()):      # 잘못된 케이스
    print('{0}: {1}'.format(dt, msg))

# dt 자체는 모듈 로딩되는 시점에 이미 datetime.now()로 할당됨
# 따라서 함수 호출 시점에, (언제 수행되던 이미 할당된 변수)를 그대로 '재사용'하게 됨


my_log("1번")    # 2024-02-20 09:45:42.695373
my_log("2번")    # 2024-02-20 09:45:42.695373    (동일)


# 해결책
def my_log2(msg, *, dt=None):
    # if not dt:
    #     dt = datetime.utcnow()
    dt = dt or datetime.utcnow()
    print('{0}: {1}'.format(dt, msg))


my_log2("1번")    # 2024-02-20 00:47:55.015727
my_log2("2번")    # 2024-02-20 00:47:55.015914


# [ Default Value 주의사항 2 ]
# - Argument 의 default Value 로 Mutable Object 사용시 주의
# - 여러번 호출하게 되는데 서로 같은 Mutable object 참조/활용하게 되어버림
def add_item(item, *, my_list=[]):
    my_list.append(item)
    return my_list


my_list = add_item('A')
print(my_list)      # ['A']

# 다른 호출
my_list2 = add_item('가')
print(my_list2)     # ['A', '가']

# 즉, my_list == mylist_2
print(my_list is my_list2)
