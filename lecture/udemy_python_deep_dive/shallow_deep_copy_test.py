# [ Shallow Copy - List (Mutable) ]

l1 = [1, 2, 3]

l2_1 = [i for i in l1]
l2_2 = l1[:]
l2_3 = l1.copy()
l2_4 = list(l1)

print(l1, l2_1, l2_2, l2_3, l2_4)
print(id(l1), id(l2_1), id(l2_2), id(l2_3), id(l2_4))

print("")


# [ Shallow Copy - Tuple (Immutable) ]
t1 = (1, 2, 3)
t2_1 = tuple(t1)
t2_2 = t1[:]

print(t1, t2_1, t2_2)
print(id(t1), id(t2_1), id(t2_2))

print("")


#  [ Shallow Copy - By Copy Module ]
import copy

# - Mutable !
l2 = copy.copy(t1)                                  # shallow copy
print(id(l1), id(l2), id(l1) == id(l2))             # 4365705408 4365658240 False

# - Immutable !
tuple2 = copy.copy(t1)
print(id(tuple2), id(t1), id(tuple2) == id(t1))     # 4365658240 4365658240 True

print("")


# [ Shallow Copy at Mutable 'Element' Object ]
v1 = [0, 0]
v2 = [0, 0]
line1 = [v1, v2]

# - Shallow + Mutable
line2 = line1.copy()
print(id(line1), id(line2))
print(id(line1[0]), id(line2[0]))                  # 동일함

# - value 변경
line1[0][0] = -1
print("\n --> original value 변경 \n")

# - 결과
print("line1: ", line1)
print("line2: ", line2)                            # line2[0] 도 같이 바뀌어버림
print("\n")


# [ Deep Copy 직접 구현 ? By Loop 등]
line2_deep_custom = [[e for e in l] for l in line2]
print("line1:", line1)
print("line_deep_custom:", line2_deep_custom)

# - value 변경
line1[0] = -888
print("\n --> original value 변경 \n")                    # line2_deep_custom[0] 변경 없음

print("line1:", line1)
print("line_deep_custom:", line2_deep_custom)
print("\n")

# - 그러나 3 depth, 4depth,.. N-Depth 이면 ? -> copy 라이브러리 활용하자!


# [ Deep Copy By 'Copy' Module ]
line2_deep_copy = copy.deepcopy(line1)
print("line1:", line1)
print("line2_deep_copy: ", line2_deep_copy)

# - value 변경
line1[0] = -999
print("\n --> original value 변경 \n")

print("line1:", line1)
print("line2_deep_copy: ", line2_deep_copy)               # line2_deep_copy[0] 변경 없음
