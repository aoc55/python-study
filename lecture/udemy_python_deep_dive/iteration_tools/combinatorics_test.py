# [ Cartesian Product ]
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c', 'd']
# - 여기서 l1과 l2의 length 가 다름

# - Nested Loop ?
def custom_product(iterable1, iterable2):
    for x in iterable1:
        for y in iterable2:
            yield x, y

my_custom_result = custom_product(l1, l2)
print(list(my_custom_result))
# [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'd'), (2, 'a'), (2, 'b'), (2, 'c'), (2, 'd'), (3, 'a'), (3, 'b'), (3, 'c'), (3, 'd')]

print("--------------------")

# - 'product' 활용
from itertools import product
product_result = product(l1, l2)
print(list(product_result))
# [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'd'), (2, 'a'), (2, 'b'), (2, 'c'), (2, 'd'), (3, 'a'), (3, 'b'), (3, 'c'), (3, 'd')]

l3 = ['ㄱ', 'ㄴ']
product_result2 = product(l1, l2, l3)
print(list(product_result2))
# [(1, 'a', 'ㄱ'), (1, 'a', 'ㄴ'), (1, 'b', 'ㄱ'), (1, 'b', 'ㄴ'), (1, 'c', 'ㄱ'),...

print("--------------------")

# [ Permutation ]
data = [1, 2, 3]
from itertools import permutations

print(list(permutations(data)))
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# - 주의사항
# - Postion 을 Uniqure 하게 동작하지, value 로 Unique 하게 동작하는게 아님
data2 = [1, 1, 1]
print(list(permutations(data2)))
# [(1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1)]

print("--------------------")

# [ Combination ]
from itertools import combinations
data = [1, 2, 3, 4, 5]
print(list(combinations(data, r=3)))
# [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]

# - 주의사항
# - 'Permutation' 처럼 Postion 을 기반으로 Unique 하게 동작하지, value 로 Unique 하게 동작하는게 아님
data2 = [1, 1, 1]
print(list(combinations(data2, r=2)))
# [(1, 1), (1, 1), (1, 1)]