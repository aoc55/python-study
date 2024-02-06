my_tuple = (
    [1, 2, 3],
    ['a', 'b', 'c']
)
print(my_tuple)
# my_tuple -> tuple -> Immutable

my_tuple[0].append(10)
my_tuple[1].append('d')
print(my_tuple)
# my_tuple 내 value 인 list -> Mutable -> 추가 가능


'''
Immutable 한 경우 Safe
'''
def my_function(s):
    s = s + " World!"
    return s

my_str = "Hello~"
my_function(my_str)
print(my_str)               # Hello~ -> 변경 없음


"""
Mutable 한 경우 Un-Safe 함
"""
def process(lst):
    lst.append(100)

my_list = [1, 2, 3]
process(my_list)
print(my_list)              # [1, 2, 3, 100] -> 변경 되어 있음


