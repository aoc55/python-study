
# [1]
# python -> do while X
# 'while True + break 구문' 패턴으로 간접 구현
def custom_do_while():

    while True:
        print("HI!")

        x = 10
        if x > 5:
            print("BREAK !!")
            break

# [2]
# while ~ else 구문
def while_else():

    x = 0
    while x < 3:
        print("in While -> ", x)
        x += 1
    else:
        print("While -> Else 구문 실행")  # break 구문 만나지 않았음 -> 수행됨


# [3]
# for ~ else 구문
def for_else():

    for x in range(3):
        if x == 2:
            break  # break 발생
    else:
        print("for -> Else 구문 실행")  # break 구문 만났음 -> 수행 되지 않음


# [4]
# for + finally
def for_and_finally():

    for x in range(5):
        try:
            if x == 3:
                print("For -> Break!")
                break
        finally:
            print("For -> Finally!") # break 구문 수행되도 finally 구문은 수행된다


# [5]
# enumerate
def for_and_enumerate():

    my_set = {1, 2, 3}
    for idx, value in enumerate(my_set): # idx, value 를 Tuple 로 리턴
        print(f'idx:{idx} value:{value}')


if __name__ == '__main__':

    custom_do_while()
    print()

    while_else()
    print()

    for_else()
    print()

    for_and_finally()
    print()

    for_and_enumerate()
    print()
