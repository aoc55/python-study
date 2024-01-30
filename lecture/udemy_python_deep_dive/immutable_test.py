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

