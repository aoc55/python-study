# [ Lambda 정의 및 호출 ]
my_lambda_func3 = lambda x: print("This is Lambda -> ", x)
my_lambda_func3(100)

# [ Lambda 실습 ]
print(lambda x: x+2)        # <function <lambda> at 0x104b84f70>


def apply_func(x, fn):
    return fn(x)


print(apply_func(1, lambda x : x *2))


# lambda x : x = 3 # No Assignemnt
# labmda x: int : x * 2 # No Assignment

# [ Lambda 실습 2]
my_func = lambda : print("hi")
my_func()

