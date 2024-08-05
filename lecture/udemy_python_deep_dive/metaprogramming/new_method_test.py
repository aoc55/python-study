# [ object.__new__ 실습 ]
class Point(object):
    pass

p = Point()
print(type(p))

p2 = object.__new__(Point)
print(type(p2))

print(type(p) is type(p2))      # True

print("--------------------------------------------------------")

# [ object.__new__ 실습2 ]
class Point(object):
    def __init__(self, x, y):
        print(" >>> init caleed ", x, y)
        self.x = x
        self.y = y


p = object.__new__(Point)
print(p.__dict__) # __init__ 호출되지 않음

# __init__ 수동 호출
p.__init__(10, 20)
print(p.__dict__)

print("--------------------------------------------------------")


# [ __new__ 오버라이딩 실습1 ]

class Point(object):
    def __new__(cls, x, y):
        print(" >>> creating instance ....", cls, x, y)
        instance = object.__new__(cls)
        return instance

    # __new__ 와 __init__ 파라미터 타입 맞으면 연속적으로 호출됨
    def __init__(self, x, y):
        print(" >>> init called ", x, y)
        self.x = x
        self.y = y

p = Point(10, 20)
print(p.__dict__)

print("--------------------------------------------------------")


# [ built-in Type 상속 시 __new__ 사용하기 ]
# - int 상속
class MySquared(int):
    def __new__(cls, x):
        return super().__new__(cls, x ** 2)


result = MySquared(4)
print(result)
print(isinstance(result, int)) # True
print()
print()

# - 반면 Built-In Type 의 경우 __init__ 에서는 커스터마이징 불가능하다
class MySquaredV2(int):
    def __init__(cls, x):
        print(" >> called init ...")
        return super().__init__(x ** 2)

try:
    result = MySquaredV2(4)
    print(result)
    print(isinstance(result, int))
except TypeError as e:
    print(e)    # object.__init__() takes exactly one argument (the instance to initialize)

print("--------------------------------------------------------")

# [ __new__ 오버라이딩 시 super().__new__(...) 사용 ]
# - V1 : object.__new__(cls) 사용
class PersonV1:
    def __new__(cls, name):
        print(f'  >> Person: __new__ {cls.__name__}...')
        instance = object.__new__(cls)
        return instance

    def __init__(self, name):
        print(f'  >> Person:: __init__ .....')
        self.name = name


class StudentV1(PersonV1):
    def __new__(cls, name, major):
        print(f'  >> Student: __new__ {cls.__name__}...')
        instance = object.__new__(cls)
        return instance

    def __init__(self, name, major):
        print(f'  >> Student:: __init__ .....')
        super().__init__(name)
        self.major = major


s = StudentV1('abc', 'math')
#   >> Student: __new__ StudentV1...
#   >> Student:: __init__ .....
#   >> Person:: __init__ .....
# - Person 에서 정의한 __new__ 호출이 생략됨을 알 수 있음

print()
print()

# - V2 : super().__new__(cls..) 사용
class PersonV2:
    def __new__(cls, name):
        print(f'  >> Person: __new__ {cls.__name__}...')
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print(f'  >> Person:: __init__ .....')
        self.name = name


class StudentV2(PersonV2):
    def __new__(cls, name, major):
        print(f'  >> Student: __new__ {cls.__name__}...')
        instance = super().__new__(cls, name)
        return instance

    def __init__(self, name, major):
        print(f'  >> Student:: __init__ .....')
        super().__init__(name)
        self.major = major


s = StudentV2('abc', 'math')

#   >> Student: __new__ StudentV2...
#   >> Person: __new__ StudentV2...
#   >> Student:: __init__ .....
#   >> Person:: __init__ .....
# - 부모에서 정의한 __new__ 도 호출 됨을 알 수 있음

