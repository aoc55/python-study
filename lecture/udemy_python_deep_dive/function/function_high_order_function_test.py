# [ Map ]
def my_func1(x):
    return x * 2


map_result1 = map(my_func1, [1, 2, 3])
print(type(map_result1))

result1 = list(map_result1)     # 최초 소모
print(result1)                  # [2, 4, 6]

result1_2 = list(map_result1)   # 한번 소모된 이후로 재사용 불가
print(result1_2)                # []


# [ Map with Lambda ]
map_result2 = map(lambda x: x * 3, [1, 2, 3])
print(list(map_result2))


# [ Map with Multi Iterables ]
print(list(map(lambda x, y: x + y, [1, 2, 3], [10, 20, 30])))


# [ Filter ]
filter_result1 = filter(lambda x: x % 2 == 0, range(10))
print(type(filter_result1))     # <class 'filter'>
print(list(filter_result1))     # [0, 2, 4, 6, 8]
print(list(filter_result1))     # [] -> 역시 소모된 이후로 재사용 불가

# [ Fitler 2 ]
# - argument 의 Func 를 None 으로 할 경우
print(list(filter(None, [0, 1, True, False, 777, None])))       # [1, True, 777]


# [ Zip ]
print(list(zip([1, 2, 3], ['가', '나', '다'])))                # [(1, '가'), (2, '나'), (3, '다')]
print(list(zip([1, 2, 3, 4, 5, 6], ['가', '나', '다'])))       # [(1, '가'), (2, '나'), (3, '다')]
print(list(zip(range(1, 100), ['가', '나', '다'])))            # [(1, '가'), (2, '나'), (3, '다')]


# [ List Comprehension ]
# - List Comprehension을 통한 Map 대체
print(list(map(lambda x: x*2, [1, 2, 3])))
print([x * 2 for x in [1, 2, 3]])

print(list(map(lambda x, y: x+y, [1, 2, 3], [10, 20, 30])))
print([x + y for x, y in zip([1, 2, 3], [10, 20, 30])])


# [ List Comprehension 2 ]
# - List Comprehension을 통한 Filter 대체
l = [1, 2, 3, 4]
print(list(filter(lambda n: n % 2 == 0, l)))
print([x for x in l if x % 2 == 0])


# [ List Comprehension 3 ]
# - List Comprehension을 통한 Map & Filter 대체
l = range(10)
print(list(filter(lambda y: y < 25, map(lambda x: x**2, l))))
print([x ** 2 for x in l if x ** 2 < 25])
