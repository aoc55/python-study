# [ Assign to Mutable Seqeunce ]
my_list = [1, 2, 3, 4, 5]
print(id(my_list), my_list)

# - Index 활용
my_list[0:2] = ['a', 'b']
print(id(my_list), my_list)

# - Slice 객체 활용
my_slice = slice(3, len(my_list))
my_list[my_slice] = ['-888', -999]
print(id(my_list), my_list)


# - Assign iterable (not sequence)
my_list[0:1] = {'set1', 'set2'}     # set -> not Sequecne
print(id(my_list), my_list)



print("")

# [ Replacing ]
# - Regular Slicing
my_list = [1, 2, 3, 4, 5]
my_list[my_slice] = ['-888', -999]

my_list[0:2] = ['a', 'b', 'c']          # 길이 맞지 않아도 됨
print(id(my_list), my_list)

# - Extended Slicing (실패)
try:
    my_list[0:5:2] = ['a', 'b', 'c', 'd']   # 길이 안 맞으면 에러
except ValueError as e:
    print(e)

# - Extended Slicing (성공)
my_list[0:5:2] = ['a', 'b', 'c']    # 길이 맞음

print("")


# [ Deleting ]
my_list = [1, 2, 3, 4, 5]
my_list[my_slice] = ['-888', -999]
print(id(my_list), my_list)


my_list[0:2] = []       # Empty List 로 Delete
print(id(my_list), my_list)

print("")


# [ Inserting Using Slices ]
my_list = [1, 2, 3, 4, 5]
print(id(my_list), my_list)

my_list[1:1] = ['new1', 'new2']
print(id(my_list), my_list)

print("")
