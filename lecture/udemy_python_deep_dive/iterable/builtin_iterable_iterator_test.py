# [ Python Built-In Iterable or Iterator ]

# - range
my_range = range(3)
print('my_range -> ', '__iter__' in dir(my_range))      # True
print('my_range -> ', '__next__' in dir(my_range))      # False
# - range :: iterable 객체로 iter 구현 및 next 미구현

# - 첫번째 사용
for x in my_range:
    print(x)

# - 두번째 사용 -> 가능!
for x in my_range:
    print(x)

# - range 의 iterator
print(type(iter(my_range)))                             # <class 'range_iterator'>

print("--------------")

# - zip
my_zip = zip([1, 2, 3], 'abc')
print('my_range -> ', '__iter__' in dir(my_zip))      # True
print('my_range -> ', '__next__' in dir(my_zip))      # True
print(my_zip is iter(my_zip))                         # True

# - 첫번째 사용
for x in my_zip:
    print(x)

# - 두번째 사용 -> Empty !! (Exhausted)
for x in my_zip:
    print(x)

print("--------------")

# [ Built-In Iterator & Lazy Evaluation ]
city_set = set()
with open('test.csv') as f:
    # f -> iterator
    print(iter(f) is f)
    print('__next__' in dir(f))

    # Lazy Evaluation
    # f 가 Iterator 이기 때문에 row 한줄씩 가져옴
    for row in f:
        city = row.strip("\n").split(",")[-1]
        city_set.add(city)

    # 한번에 가져온다 ? 메모리에 모두 로딩해야함
    # all_rows = f.readlines()
    # print(all_rows)

print("City Set =>", city_set)
