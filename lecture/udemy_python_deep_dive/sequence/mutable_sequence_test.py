# [ Mutable Sequence Type ]
# - 대표적인 예시로 list, set, ...
my_list_0 = [1, 2, 3, 4, 5]
print(id(my_list_0))                # 4346782080

# - 변경 후에도 ID 그대로 유지
my_list_0[0] = -1
print(id(my_list_0))                # 4346782080


# [ Mutable Sequence Type 2 ]
# - 동일한 객체 참조
my_list1 = ['a', 'b', 'c', 'd']
my_list2 = my_list1
my_list1.clear()
print(id(my_list1), id(my_list2), id(my_list1) == id(my_list2))
print(my_list1, my_list2)


# [ Mutation or NOT Mutation ]
# - NOT Mutation
# - ID 가 전후 다름
my_list_1 = [1, 2, 3]
print(id(my_list_1))                # 4338606272
my_list_1 = my_list_1 + [4]
print(id(my_list_1))                # 4338607872

# - Mutation
# - ID 가 전후 같음
my_list_2 = [1, 2, 3]
print(id(my_list_2))                # 4365312320
my_list_2.append(4)
print(id(my_list_2))                # 4365312320


# [ Mutalbe Sequence Type 에서 제공하는 메소드 실습 ]
my_list3 = ['a', 'b', 'c']
my_list3.extend(['d', 'e'])
print(my_list3)

my_list3.extend({'z', 'f', 'g'})    # set()의 경우 순서 미보장 주의
print(my_list3)                     # ['a', 'b', 'c', 'd', 'e', 'z', 'g', 'f'] -> f랑 g 순서 변경

print(my_list3.pop())

my_list3.insert(0, 'ㄱ')

print("before reverse -> ", my_list3)
my_list3.reverse()  # inplace - sort
print("after reverse -> ", my_list3)


# [ Mutalbe Sequence Type 에서 제공하는 Copy 실습 ]

l1 = [['a', 'b'], 'c', 'd']
l2 = l1.copy()
print(id(l1), id(l2), id(l1) == id(l2))                     # False 동일하지 않음

# - 단, shallow copy 로 인해서 item 에 대한 참조(?) 동일
print(id(l1[0]), id(l2[0]), id(l1[0]) == id(l2[0]))         # True 동일함

