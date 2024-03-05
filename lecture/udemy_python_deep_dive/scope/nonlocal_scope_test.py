# [ Non-Local Scope #1 ]
# - 중첩된 함수 정의 시 발생
def outer_fuc_1():
    a = 10

    def inner_func_1():
        print(a)            # inner 입장에서 'a'는 non-local scope 내 변수

    inner_func_1()


outer_fuc_1()


# [ Non-Local Scope #2-1 ]
# - NonLocal 변수 수정 시도
def outer_fuc_2_1():
    a = 10

    def inner_func_2_1():
        a = -1                  # 수정 ? X -> Local Scope 변수 새로 Assgin
        print(f'inner a={a}')


    inner_func_2_1()

    print(f'outer a={a}')


outer_fuc_2_1()


# [ Non-Local Scope #2-2 ]
# - 'nonlocal' Keyword 를 사용해 NonLocal 변수 수정
def outer_fuc_2_2():
    a = 10

    def inner_func_2_2():
        nonlocal a              # 선언
        a = -1                  # 수정 ? X -> Local Scope 변수 새로 Assgin
        print(f'inner a={a}')

    inner_func_2_2()

    print(f'outer a={a}')


outer_fuc_2_2()


# [ Non-Local Scope #3 ]
# - 중첩의 중첩 구조
def outer_func_3():
    a = 10

    def inner_3_1():        # 중첩1
        def inner_3_2():    # 중첩2
            nonlocal a
            a = -2

        inner_3_2()

    inner_3_1()
    print(f'Nested outer a={a}')


outer_func_3()


# [ Non-Local Scope #4 ]
# - 중첩의 중첩 구조 + nonlocal 연쇄사용
def outer_func_4():
    a = 10

    def inner_4_1():        # 중첩1
        nonlocal a

        def inner_4_2():    # 중첩2
            nonlocal a
            a = -3

        inner_4_2()

    inner_4_1()
    print(f'Nested outer a={a}')


outer_func_4()


# [ Global & Non-Local Scope ]
# - 중첩된 함수 + Global
x = 777
def outer_fuc_6():
    x = 'python'            # Global 이 아닌, 자체 Local 변수

    def inner_func_6_1():
        nonlocal x          # Global 이 아닌, outer 의 Local 변수의미
        x = 'hi'

        def inner_func_6_2():
            global x        # Global 변수 의미
            x = 'hello'

        inner_func_6_2()

    inner_func_6_1()
    print(f'outer x={x}')


outer_fuc_6()
print(f'global x={x}')
