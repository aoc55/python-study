# [ Slots 기본 테스트 ]
class Location:
    __slots__ = ['name', '_longitude', '_latitude']

    def __init__(self, name, *, longitude, latitude):
        # 초기화는 동일하게 ..
        self._longitude = longitude
        self._latitude = latitude
        self.name = name

    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude(self):
        return self._latitude


# - Class 레벨?  -> X
print(Location.__dict__)
Location.new_property = 'new_property_value'
print('new_property' in Location.__dict__)  # True
print()

# - Instnace 레벨 !! -> O
loc = Location('seoul', latitude=19.0677, longitude=72.07777)
print(loc.name, loc.latitude, loc.longitude)
print()

# - attribute del, update 등 가능
del loc.name
loc.name = 'new-name'
print(loc.name)
loc.name = 'update-name'
print(loc.name)

# - __dict__ 미구성
try:
    print(loc.__dict__)
except AttributeError as e:
    print(e)  # 'Location' object has no attribute '__dict__'
print()

# - 새로운 attribute assign 불가
try:
    loc.new_property = 'new_property_value'
except AttributeError as e:
    print(e)    # 'Location' object attribute 'new_property' is read-only
print()

print("----------------------------------")


# [ Slots & Single Inheritance 1 - 부모에만 slots ]
class Person:
    __slots__ = 'name',

    def __init__(self, name):
        self.name = name


class Student(Person):
    pass


# - slots 에 정의한 속성은 slots 에 저장
s = Student('Eric')
print(s.name)
print('name' in s.__dict__)         # False

# - 자식 클래스 자체에서 instance dict 생성
# - 이후 추가적인 속성은 instance dict 에 저장
s.age = 'new-age'
print('age' in s.__dict__)          # True
print(s.__dict__)


# [ Slots & Single Inheritance 2 - 자식에만 slots ]
class Person:

    # 부모는 instance dir 기반
    def __init__(self, name):
        self.name = name


class Student(Person):

    # 자식은 slot 기반
    __slots__ = ['school', 'student_number']

    def __init__(self, name, school, student_number):
        super().__init__(name)                  # instance dir
        self.school = school                    # slots
        self.student_number = student_number    # slots


s = Student('james', 'MI6', '007')
print(s.name, s.school, s.student_number)      # 사용 방식에는 동일
print(s.__dict__)
print('name' in s.__dict__)                    # True

print("----------------------------------")


# [ Slots & Single Inheritance 3 - 부모 & 자식 모두 slots ]
class Person:

    # slot 기반
    __slots__ = 'name',

    def __init__(self, name):
        self.name = name


class Student(Person):

    # slot 기반
    __slots__ = ['school', 'student_number']

    def __init__(self, name, school, student_number):
        super().__init__(name)
        self.school = school
        self.student_number = student_number


s = Student('james', 'MI6', '007')
print(s.name, s.school, s.student_number)

try:
    print(s.__dict__)
except AttributeError as e:
    print(e)


print("----------------------------------")


# [Slots & Single Inheritance 4 - 활용팁 모두 사용하기 ]
class PersonFinal:
    __slots__ = ['name', '__dict__']

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = PersonFinal('Alex', 10)

# - in slots
print(p.name, p.age)
print('name' in p.__dict__)     # False

# - 새로운 attribute -> instance dict
print(p.__dict__)
p.new_attr = 'new_attr'
print('new_attr' in p.__dict__)


