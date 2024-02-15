# [ * 를 통한 Unpacking 1]
my_list = [-10, 5, 2, 100]
a1, *b1 = my_list
a2, b2 = my_list[0], my_list[1:]
print(a1 == a2, b1 == b2)     # True, True

my_str = "HELLO"
a, *b, c = my_str
print(a == 'H', b == ['E', 'L', 'L'], c == 'O')

# [* 를 통한 UnPacking 2]
# - Un-Orderd Type 도 지원가능하다 (not Indexable)
# - Slicing 이 안되지만 Unpacking 을 활용할 수 있음
my_set = {1, 2, 3}          # Set 도 가능 (Unordered Type)
a, *b = my_set              # 단, 순서는 보장하지 않는다
print(b)                    # 결과는 List

my_str = "hello~"           # String 도 가능
a, *b = my_str
print(b)                    # 결과는 List

# * Operator Left(LHS) 쪽에는 한번만 사용가능
# a, *b, *c = "hello"  ->  불가


# [ * 를 통한 Merge ]
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [*l1, *l2]             # * Operator Right(RHS) 쪽에는 여러번 사용 가능
print(l3)

l1 = [1, 2, 3]
str1 = 'ABCD'
l3 = [*l1, *str1]
print(l3)                   # [1, 2, 3, 'A', 'B', 'C', 'D']


# [** 를 통한 UnpPacking & Merge]
# - dict 타입을 위한 **
# - key, value 구조로 Unpakcing 활용 가능
# - 단, 순서는 보장되지 않는다

my_dict = {
    'k1': 'v1',
    'k2': 'v2'
}

my_dict2 = {
    'k2': 'p2',
    'k3': 'p3'
}

my_dict3 = {**my_dict, **my_dict2}
print(my_dict3)
print(my_dict3['k2'] == 'p2')           # Key 중복 시? 값 마지막 값으로 override 됨


#  [ Nested Unpacking ]
# - Nested 의 경우 LHS에 * 중첩 사용 가능
a, *b, (*c, d) = [1, 2, 3, 'python']
print(b == [2, 3])
print(c == ['p', 'y', 't', 'h', 'o'])

