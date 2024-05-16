# [ Iterator 를 Method 의 Argument 로 사용하지 않기 ]
# - 깜빡하기 쉬운데, 의도하지 않은 동작 많이 발생할 수 있음

def my_func(data):                  # iterator 전달시?
    max_value = get_max(data)
    min_value = get_min(data)
    return max_value, min_value


def get_max(data):
    max_value = max(list(data))
    print("get_max result = ", max_value)
    return max_value


def get_min(data):
    min_value = min(list(data))
    print("get_min result = ", min_value)
    return min_value

iter_my_list = iter([1, 2, 3, 4, 5])
try :
    result = my_func(iter_my_list)      # iterator 를 함수에 전달
    print(result)
except ValueError as e:
    print(e)            # min() arg is an empty sequence
    # - 즉, Max 에서 이미 iterator 모두 소모함
    # - Min 에서는 Empty 에 따라 오류 발생
    # - 따라서 Argument 로는 Iterator 를 넣지 말자


print("----------------------------------------")


# [ 개선안 - Iterator 예외처리 ]
def my_func_v2(data):
    if data is iter(data):
        raise ValueError("No Iterator as Parameter")  # iterator 전달시 예외처리?

    max_value = get_max(data)
    min_value = get_min(data)
    return max_value, min_value


iter_my_list = iter([1, 2, 3, 4, 5])
try:
    result = my_func_v2(iter_my_list)      # iterator 를 함수에 전달
    print(result)
except ValueError as e:
    print(e)            # 예외처리 동작


print("----------------------------------------")

# [ 개선안2 - Collection 으로 옮겨담기 ]
def my_func_v3(data):
    data = list(data)           # iterator -> collection 으로 옮겨 담기
    max_value = get_max(data)   # 단, 하위 메서드 시 다시 Iterator 변경됨
    min_value = get_min(data)
    return max_value, min_value


iter_my_list = iter([1, 2, 3, 4, 5])
try:
    result = my_func_v3(iter_my_list)      # iterator 를 함수에 전달
    print(result)                          # 정상수행됨
except ValueError as e:
    print(e)

