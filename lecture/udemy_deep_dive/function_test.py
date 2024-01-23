
# [1]
def my_func0():
    print("sample function")


# [2]
# 호출 전까지 정의는 됨
def my_func1():
    no_defined_func()


# [4]
# Parameter 에 Annotation 설정
def my_func_4(x: int, y: int):
    print(x * y)


if __name__ == '__main__':

    # [1]
    # Function => Object!
    print(my_func0)     # <function my_func0 at 0x102623ee0>

    # [2]
    # 호출 시 실패 발생
    try:
        my_func1()
    except NameError as e:
        print("Name Error => ", e)

    # [3]
    # Lambda 정의 및 호출
    my_lambda_func3 = lambda x: print("This is Lambda -> ", x)
    my_lambda_func3(100)

    # [4]
    my_func_4(10, 20)  # 정상
    my_func_4("MY-STR", 3)  # IDE 에서 Warning 처리는 해주나 파이썬에서 막지는 않음
    try:
        my_func_4("X", "Y")
    except TypeError as e:
        print("Type Error => ", e)


