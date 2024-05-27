# [ Zip ]
# - 'Shortest' 기반의 Zip
l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4]
l3 = [1, 2, 3]

basic_zip_result = zip(l1, l2, l3)
print(iter(basic_zip_result) is basic_zip_result)
print('__next__' in dir(basic_zip_result))

print(list(basic_zip_result))           # 제일 짧은 Itrable 기준으로 동작
# [(1, 1, 1), (2, 2, 2), (3, 3, 3)]

print("----------------------")

# [ Longest Zip ]
from itertools import zip_longest
longest_zip_result = zip_longest(l1, l2, l3)
print(iter(longest_zip_result) is longest_zip_result)
print('__next__' in dir(longest_zip_result))

print(list(longest_zip_result))
# [(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, None), (5, None, None)]

print("----------------------")


# [ Longest Zip 2 ]
# - with 'fill value'
from itertools import zip_longest
longest_zip_result2 = zip_longest(l1, l2, l3, fillvalue="-1")       # 'fillvalue 설정'
print(iter(longest_zip_result2) is longest_zip_result2)
print('__next__' in dir(longest_zip_result2))

print(list(longest_zip_result2))
# [(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, '-1'), (5, '-1', '-1')]

