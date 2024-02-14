# [ Function is Object !! ]
def my_func_1():
    print("hello")


print(id(my_func_1))    # 함수에 할당된 메모리 주소 조회

# [ Function 다른 함수에 Assign 될 수 있음 ]
a = my_func_1
a()     # 호출


# [ 다른 함수의 파라미터로 사용 될 수 있음 ]
def my_func_2(fn):      # 파라미터로 함수를 받는다
    fn()


my_func_2(my_func_1)    # 파라미터로 함수를 전달


# [ 함수 반환 값으로 함수 가능 ]
def my_func3():
    return my_func_1    # 리턴으로 함수 전달


b = my_func3()
b()                     # 리턴 받은 함수 호출

