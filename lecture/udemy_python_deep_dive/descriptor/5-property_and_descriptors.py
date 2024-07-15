from numbers import Integral

# [ property & Descriptor 실습1 ]
# - @property Decorate Version
class Person:

    @property
    def age(self):
        print(" >> age.getter")
        return getattr(self, '_age', None)

    @age.setter
    def age(self, value):

        print(" >> age.setter")

        # Validation
        if not isinstance(value, Integral):
            raise ValueError('age: must be an Integer')
        if value < 0:
            raise ValueError(' 0보다 크거나 같아야 함')

        # 값 세팅
        self._age = value


p = Person()
p.age = 10          # setter 호출
print(p.__dict__)   # {'_age': 10}
print("")

# - 'property' class 활용 시 => Descriptor protocol 구현?
print(hasattr(Person.age, '__get__'))       # True
print(hasattr(Person.age, '__set__'))       # True
print(hasattr(Person.age, '__delete__'))    # True


print("-------------------------------")

# [ property & Descriptor 실습2 ]
class PersonV2:

    def get_age(self):
        print("  >> get_age")
        return getattr(self, '_age', None)

    def set_age(self, value):
        print("  >> set_age")

        if not isinstance(value, Integral):
            raise ValueError('age: must be an Integer')
        if value < 0:
            raise ValueError(' 0보다 크거나 같아야 함')

        self._age = value

    # Decorater 가 아닌 직접 선언
    age = property(fget=get_age, fset=set_age)


# - Property Class 확인
print("PersonV2.age =>", PersonV2.age)
print()

p2 = PersonV2()
p2.age = 10             # set_age 호출
print(p2.__dict__)      # {'_age': 10}
print()

# - 'property' class 활용 시 => Descriptor protocol 구현?
print(hasattr(PersonV2.age, '__get__'))
print(hasattr(PersonV2.age, '__set__'))
print(hasattr(PersonV2.age, '__delete__'))


print("-------------------------------")

# [ property & Descriptor 실습3 ]
# - setter 는 미구현!
class TimeUTC:

    @property
    def current_time(self):
        return "Current Time Demo"

    # -> setter 미구현

t = TimeUTC()
print(t.current_time)           # get 호출

try:
    t.current_time = 'other'    # set 호출
except AttributeError as e:
    print(e)
print()

print("-------------------------------")
# [ property & Descriptor Shadow 실습 ]
# - Data Descriptor 인 경우

p = Person()
print(p.__dict__)       # {}
print()

p.age = 10              #  >> age.setter
print(p.__dict__)       # {'_age': 10}
print()

# instance Dict 에서 직접 정의
p.__dict__['age'] = 888
print(p.__dict__)       # {'_age': 10, 'age': 888}
print()

# 호출 -> Instance Dict 가 아닌 Descriptor 통해서 호출
print(p.age)             #  >> age.getter 10


print("-------------------------------")

# [ property 클래스 직접 만들어보기 ]

# - Custom Property 클래스 정의
# - Descriptor 프로토콜 구현
class MakeProperty:

    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset

    def __set_name__(self, owner, name):
        self.prop_name = name

    def __get__(self, instance, owner):
        print(' >>> MakeProperty  __get__ called ...')

        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError(f'{self.prop_name} is not Readable')

        return self.fget(instance)

    def __set__(self, instance, value):
        print(' >>> MakeProperty  __set__ called ...')

        if self.fset is None:
            return AttributeError(f'{self.prop_name} is not Wirteable')

        self.fset(instance, value)


class PersonV3:

    def get_name(self):
        print('>> get_name called ...')
        return getattr(self, '_name')

    def set_name(self, value):
        print('>> set_name called ...')
        self._name = value

    # 직접 정의한 Property 클래스 사용
    name = MakeProperty(fget= get_name, fset=set_name)


p = PersonV3()
p.name = 10             # getter
print(p.name)           # setter
print(p.__dict__)       # {'_name': 10}
print("")


# Instance Dict Shadow 테스트
p.__dict__['name'] = 'aaaaaa'
print(p.__dict__)   # {'_name': 10, 'name': 'aaaaaa'}
print()

# 조회 -> 역시 Data - Descripotr Protocol 구현한 MakeProperty 함수 호출
print(p.name)

