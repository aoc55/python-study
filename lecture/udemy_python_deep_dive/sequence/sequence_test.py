# [ Sequence 실습 1 ]
my_list = ['a', 'b', 'c']

for s in my_list:
    print(s)

# [ Sequence 실습 2 ]
# - Immutable vs Mutalbe
my_list = ['a', 'b', 'c']
my_list[2] = 'x'

my_tuple = (1, 2, 3)
try:
    my_tuple[2] = -1
except TypeError as e:
    print(e)

# [ Sequence 실습 3 ]
comparable_sequence = [1, 2, 3]
comparable_sequence2 = [1, 2.5, -10.2]
not_comparable_sequence = [1 + 1j, 2 + 2j, 3 + 3j]
not_comparable_sequence_2 = [10, 'a', 10.5]

# - 가능
min(comparable_sequence)
max(comparable_sequence2)

# - 불가
try:
    min(not_comparable_sequence)
except TypeError as e:
    print(e)

try:
    min(not_comparable_sequence_2)
except TypeError as e:
    print(e)

# [ Sequence 실습 4 ]
# - concat, repeat 시 주의사항
x = [1, 2]
a = [x]

concat_a = a + a

concat_a[0][0] = -1
print(concat_a)
# [[-1, 2], [-1, 2]]

a = [x]
repeat_a = a * 2
repeat_a[0][0] = -1
print(repeat_a)
# [[-1, 2], [-1, 2]]


# [ Sequence 실습 5 ]
# - indexing
my_str = "abcbabbbda"

print(my_str.index('a'))                        # 0
print(my_str.index('a', 2))     # 4
print(my_str.index('a', 5))     # 9

# - 없으면 예외
try:
    print(my_str.index("z"))
except ValueError as e:
    print(e)

# [ Sequence 실습 6 ]
# - slicing
# - slicing 할때마다 새로운 Object 반환
my_list = ['a', 'b', 'c']
sliced_1 = my_list[:2]
sliced_2 = my_list[:2]
print(sliced_1 == sliced_2)                                         # True
print(id(sliced_1), id(sliced_2),  id(sliced_1) == id(sliced_2))    # 4369183808 4369278272 False


