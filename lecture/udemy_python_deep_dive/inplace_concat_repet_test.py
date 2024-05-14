# [ Concat - Mutable ]
l1 = [1, 2, 3, 4]
l2 = [5, 6]

print(id(l1), l1)
print(id(l2), l2)

l1 = l1 + l2
print(id(l1), l1)           # id(l1) 변경되어 있음 -> 새로운 객체
print("")

# [ In-place Concat - Mutable ]
l1 = [1, 2, 3, 4]
l2 = [5, 6]
print(id(l1), l1)
print(id(l2), l2)
l1 += l2
print(id(l1), l1)           # id(l1) 변경 X -> l1 객체 그대로 "in-place"
print("")


# [ Concat, In-place Concat - Immutable)
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(id(t1), t1)
print(id(t2), t2)

t1 = t1 + t2
print(id(t1), t1)           # id(t1) 변경되어 있음 -> 새로운 객체
print("")

t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(id(t1), t1)
print(id(t2), t2)

t1 += t2
print(id(t1), t1)           # # id(t1) 변경되어 있음 -> 새로운 객체 (in-place 여도 immutable 함으로
print("")


# [ In-place concat List + Tuple ]
l1 = [1, 2, 3, 4]
t1 = (5, 6)
print(id(l1), l1)
print(id(t1), t1)

l1 += t1
print(id(l1), l1)           # 기존 id(l1) 변경 X
print("")


# [ Repetition - Immutable]
l1 = [1, 2, 3, 4]
print(id(l1))

l1 = l1 * 2
print(id(l1))               # id(l1) 변경되어 있음 -> 새로운 객체
print("")

# [ In-place Repettion - Mutable ]

l1 = [1, 2, 3, 4]
print(id(l1))

l1 *= -1
print(id(l1))               # id(l1) 변경되어 있지 않음 (In-place)
