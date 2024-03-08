# [ Free Variable 수정 ]
def counter():
    count = 0

    def inc():
        nonlocal count  # Free Variable 수정하기 위한 nonlocal 키워드 선언
        count += 1
        return count

    return inc  # 함수 리턴


fn = counter()      # fn -> Closure()
print(fn())
print(fn())
print(fn.__code__.co_freevars)  # ('count',)


# [ Cell 구조 확인 ]
def outer_0():
    n0 = 100
    print(f'at Outer : {hex(id(n0))}')

    def inner_0():
        print(f'at inner_0 : {hex(id(n0))}')

    return inner_0


fn0 = outer_0()             # at Outer : 0x100b415d0
fn0()                       # at inner_0 : 0x100b415d0
print(fn0.__closure__)      # (<cell at 0x102acbc70: int object at 0x1028255d0>,)
# - Indirect Reference 통해서 동일 참조중


# [ Nested Closure ]
def incrementer(n):

    # inner() + n => Closure
    def inner(start):
        current = start

        # inc() + current + n => Closure
        def inc():
            nonlocal current
            current += n
            return current

        return inc

    return inner


fn = incrementer(2)
inc_2_from_100 = fn(100)
print(inc_2_from_100() == 102)               # 함수 호출 시점에 변수들의 값 (2, 100..)을 숨길 수 있음
print(inc_2_from_100() == 104)


# [ Shared Extended Scope ]
def outer_1():
    count = 0       # Free Variable

    # inc_1, inc_2 동일 Free Variable 참조 및 수정
    def inc_1():
        nonlocal count
        count += 1
        return count

    def inc_2():
        nonlocal count
        count += 1
        return count

    return inc_1, inc_2


fn_1_1, fn_1_2 = outer_1()
print(fn_1_1())
print(fn_1_2())

# - 동일 Cell (-> 동일 Object) 참조중임
print(fn_1_1.__closure__)   # (<cell at 0x104c838b0: int object at 0x1049ae950>,)
print(fn_1_2.__closure__)   # (<cell at 0x104c838b0: int object at 0x1049ae950>,)


# [ Shared Extended Scope 2-0 ]
# - 각기 다른 Free Variable & Scope
def adder(n):
    # n -> Free Variable
    def inner(x):
        return x + n
    return inner


add_1 = adder(1)
add_2 = adder(1)
add_3 = adder(1)

# 각기 다른 Cell 객체를 통해서 Singletone 인 11(0x104a56930) 가리키고 있음
print(add_1(10))
print(add_1.__closure__)    # (<cell at 0x104d2b820: int object at 0x104a56930>,)

print(add_2(10))
print(add_2.__closure__)    # (<cell at 0x104d2b7f0: int object at 0x104a56930>,)

print(add_3(10))
print(add_3.__closure__)    # (<cell at 0x104d2b730: int object at 0x104a56930>,)


# [ Shared Extended Scope 2-1 ]
# - 주의사항 예시 (아래와 같이 구현하면 안됨)
# - 뭔가 반복문으로 자동화??
adders = []
for n in range(1, 4):
    adders.append(lambda x: x + n)      # n 은 Global Variable (lambda 외부인 모듈레벨에서 정의됨)

print(adders[0](10))    # 13
print(adders[1](10))    # 13
print(adders[2](10))    # 13
# - address 배열 내에 있는 Lambda 함수가 '호출될때' -> Global Variable n 에 대해 평가
# - 따라서 호출 시점에는 이미 n 이 range(1,4)에 의해 3로 도달
# - 그래서 모두 결과가 3 + 10 으로 같음


# [ Shared Extended Scope 2-2 ]
# - 주의사항 예시2 (아래와 같이 구현하면 안됨)
def create_adders():
    my_adders = []
    for n2 in range(1, 4):
        my_adders.append(lambda x: x + n2)        # n2 는 Free Variable (create_adders의 Local Variable)
    return my_adders


adders2 = create_adders()
print(adders2[0](10))    # 13
print(adders2[1](10))    # 13
print(adders2[2](10))    # 13
# - 위 예시 1과 결과 동일함
# - 원인도 동일함 (호출시점에 Free Variable 평가된다)
# - 따라서 동일한 n2 통해서 Cell 을 가르킴 (의도한 대로 각각이 아니라_


# [ Shared Extended Scope 2-3 ]
# - 해결책 ?
# - Lambda 와 Closure 는 다르다!
def create_adders_solution():
    my_adders = []
    for n3 in range(1, 4):

        # Function (Lambda) 의 Default Value 로 활용하기
        # 왜냐? Default Value 는 함수가 정의되는 시점에 평가되므로!!!
        my_adders.append(lambda x, y=n3: x + y)     # y는 Free Variable 가 아니다

    return my_adders


adders3 = create_adders_solution()
print(adders3[0](10))    # 11
print(adders3[1](10))    # 12
print(adders3[2](10))    # 13
print(adders3[0].__closure__)           # None
