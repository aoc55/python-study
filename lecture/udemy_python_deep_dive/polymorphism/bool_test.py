# [ Collection Type -> bool 미 구현 ]
class MyCustomList:

    def __init__(self, length):
        self._length = length

    def __len__(self):
        print(">> __len__ called")
        return self._length

    # __bool__ 미구현


l1 = MyCustomList(10)
l2 = MyCustomList(0)


print(bool(l1))          # '>> __len__ called' -> True
print(bool(l2))          # '>> __len__ called' -> False


print("-------------------------")


# [ Collection Type -> bool 구현 ]
class MyCustomListV2:

    def __init__(self, length):
        self._length = length

    def __len__(self):
        print(">> __len__ called")
        return self._length

    # - bool 구현 시 이것부터 실행됨
    def __bool__(self):
        print(">> __bool__ called")
        return self._length > 0


l1 = MyCustomListV2(10)
l2 = MyCustomListV2(0)

print(bool(l1))             # '>> __bool__ called' -> True
print(bool(l2))             # '>> __bool__ called' -> False


print("-------------------------")


# [ 일반 Type 의 Bool 미 구현 ]
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __bool__(self):


p1 = Point(0, 0)
p2 = Point(1, 1)

print(bool(p1), bool(p2))       # True, True


print("-------------------------")


# [ 일반 Type 의 Bool 구현 ]
class PointV2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __bool__(self):
        # return self.x != 0 or self.y != 0
        return bool(self.x or self.y)


p1 = PointV2(0, 0)
p2 = PointV2(1, 1)

print(bool(p1), bool(p2))       # False True
