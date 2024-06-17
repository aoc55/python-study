
data = [1, 2, 3, 4, 5]

"Itertools!!"

# Permutation
from itertools import permutations

result_list = list(permutations(data))       # 생략 시 입력 값의 길이의 순열
print(len(result_list))
print(list(result_list))
print("-----")

result_list = list(permutations(data, 2))  # 길이 2인 순열
print(len(result_list))
print(list(result_list))
print("-----")

# Combination
from itertools import combinations
result_list = list(combinations(data, 2))
print(len(result_list))
print(list(result_list))
print("-----")


result_list = list(combinations(data, 5))
print(len(result_list))
print(list(result_list))
print("-----")


# [Product]
# - 1개 이상의 'iterable' 간에 곱집합 생성
from itertools import product

data1 = [1, 2, 3, 4, 5]
data2 = ['가', '나', '다']

result_list = list(product(data1, data2))
print(len(result_list))
print(result_list)
