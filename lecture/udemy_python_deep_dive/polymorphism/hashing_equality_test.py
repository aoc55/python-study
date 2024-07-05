# [ 기본 Class - 별도 미구현 ]
class Person:
    pass
    # eq, hash 미구현


p1 = Person()
p2 = Person()


print(p1 == p2)                 # False
print(p1 is p2)                 # False
print(hash(p1), hash(p2))       # 기본 ID 로 사용 273462245 273462242

print("-------------------------")


# [ 'eq' 함수만 구현 ]
class PersonV2:
    def __init__(self, name):
        self.name = name

    # - eq 정의
    def __eq__(self, other):
        return isinstance(other, PersonV2) and self.name == other.name

    # - hash 는 미 정의
    # def __hash__(self):

    def __repr__(self):
        return f'Person(name="{self.name}")'


p1 = PersonV2('abc')
p2 = PersonV2('abc')

print(p1 == p2)
print(p1 is p2)

# - hash 함수 시도 시 Type Error 발생
try:
    print(hash(p1))
except TypeError as e:
    print(e)

# - eq 함수만 구현시 hash 함수의 경우 NonType !! -> 사용불가
print(type(p1.__hash__))        # <class 'NoneType'>


print("-------------------------")


# [ 'eq' 함수 및 'hash' 구현 ]
class PersonV3:
    def __init__(self, name):
        # Immutable 하기 위해서?
        self._name = name

    @property
    def name(self):
        return self._name

    # - eq 정의
    def __eq__(self, other):
        return isinstance(other, PersonV2) and self.name == other.name

    # - hash 도 정의
    def __hash__(self):
        return hash(self._name)

    def __repr__(self):
        return f'Person(name="{self.name}")'


p1 = PersonV3('abc')
p2 = PersonV3('abc')

print(p1 == p2)
print(p1 is p2)

# - hash 함수 호출가능
print(hash(p1), hash(p2))
print(type(p1.__hash__))        # <class 'method'>

# - dict key 등에 -> 이제 사용 가능 !!
my_dict = {p1: True}
print(my_dict)

my_set = {p1}
print(my_set)
