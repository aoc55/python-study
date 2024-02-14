# [ 함수 정의 기초 ]
def my_func0():
    print("sample function")


# Function -> Object !!
print(my_func0)     # <function my_func0 at 0x102623ee0>


# [ 유효하지 않은 함수 정의 ]
# 정의 자체는 된다
def my_func1():
    no_defined_func()


# 실제 호출 시 에러 발생
try:
    my_func1()
except NameError as e:
    print("Name Error => ", e)


# [ Parameter 에 Annotation 설정 ]
def my_func_4(x: int, y: int):      # :int -> 'Annotation'
    print(x * y)


my_func_4(10, 20)  # 정상

# IDE 에서 Annotation 에 대한 Warning 처리는 해주나 파이썬에서 막지는 않음
my_func_4("MY-STR", 3)

try:
    my_func_4("X", "Y")
except TypeError as e:
    print("Type Error => ", e)


# [ Lambda 정의 및 호출 ]
my_lambda_func3 = lambda x: print("This is Lambda -> ", x)
my_lambda_func3(100)
