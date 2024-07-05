# [ Method 를 통한 Attribute(Instance Property) 접근 ]
# - Property 클래스 사용하기 전에 직접 구현해보기
class Person:
    def __init__(self, name):
        # Attribute 선언
        self.set_name(name)

    # 접근용 Method
    def get_name(self):
        return self._name

    # 설정용 Method
    def set_name(self, name):
        if isinstance(name, str) and len(name.strip()) > 0:
            self._name = name.strip()
        else:
            raise ValueError("Name Not Valid")


# 테스트
try:
    Person('')
except ValueError as e:
    print(e)
print("")

p = Person("kgh")
print(p.get_name())
print(p.__dict__)   # {'_name': 'kgh'}

p.set_name("new_name")
print(p.__dict__)   # {'_name': 'new_name'}


print("------------------------------")

# [ Property 클래스를 활용한 Instance Proeprty 정의 ]

class PersonV2:
    """This is a Person Object (DocString)"""
    def __init__(self, name):
        self.set_name(name)

    def get_name(self):
        print(" >> getter called")
        return self._name

    def set_name(self, name):
        print(" >> setter called")
        if isinstance(name, str) and len(name.strip()) > 0:
            self._name = name.strip()
        else:
            raise ValueError("Name Not Valid")

    def del_name(self):
        print(" >> delete called")
        del self._name

    # property 선언
    name = property(fget=get_name, fset=set_name, fdel=del_name, doc="The Person's name")


# 활용
p2 = PersonV2('kgh2')

# - property 통한 접근
p2.name = 'ok'          # using 'name' property 의 'fset'
print(p2.name)          # using 'name' property 의 'fget'

# - getattr, settattr 에도 동일하게 적용
print(getattr(p2, 'name'))
setattr(p2, 'name', 'zzz')

# namespace 조회
print(p2.__dict__)          # {'_name': 'ok'}
print(PersonV2.__dict__.get('name'))    # <property object at 0x1047f4a90>

del p2.name


print("------------------------------")

# [ Property 클래스 ]
print(type(property()))     # property 역시 클래스임
print("")

# - Property 생성해보기
p = property(lambda self: print('hi'))
print(property.__dict__)

print("------------------------------")


# [ 데코레이터 복습 ]
def my_decorator(fn):
    print("---> decorating function")

    def inner(*args, **kwargs):
        print("--> running decorated function")
        return fn(*args, **kwargs)

    return inner


def original_func(a, b):
    print("--> Original Function")
    return a + b


decorate_func = my_decorator(original_func)
decorate_func(1, 3)

# - 보통은 이렇게 덮어쓰기
original_func = my_decorator(original_func)
original_func(1, 3)
print(original_func)

# - 데코레이터 기반
@my_decorator
def original_func2(a, b):
    print("--> Original Function 2")
    return a + b


original_func2(3, 5)

print("------------------------------")


# [ Property 클래스 실습 ]
def get_prop(self):
    print('--> getter called')


def set_prop(self):
    print('--> setter called')


def del_prop(self):
    print('--> deleter called')


# - property 직접 생성
my_property = property(fget=get_prop)

# - setter 설정 -> 새로운 property 생성
my_property_2 = my_property.setter(set_prop)
print(my_property is my_property_2)              # False -> 새로운 Property 생성
print(my_property.fget is my_property_2.fget)    # True -> 단, 바라보고 있는 함수는 동일

# - 데코레이터 동작 방식
# - 계속 동일 변수에 덮어쓴다
p = property(get_prop)
p = p.setter(set_prop)
p = p.deleter(del_prop)


# [ 데코레이터 기반의 Proeprty 설정 1 ]
class PersonFinal:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):      # 함수 이름 property 동일하게 해야함
        self._name = value


# - 활용
p = PersonFinal('abbbbb')
print(p.name)
p.name = 'xxx'
print(p.name)

print(PersonFinal.name)


# [ 데코레이터 기반의 Proeprty 설정 2 ]
# - only setter 만하고 싶을때
class PersonFinalV2:

    my_property = property(doc='write-only prorperty')

    @my_property.setter
    def my_property(self, value):
        print('setter called')


print("------------------------------")


# [ Properties 제거하기 ]
# - Runtime 에 Properties 제거하기
class Circle:
    def __init__(self, color):
        self._color = color
        self.temp1 = 'temp1'

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @color.deleter
    def color(self):
        del self._color


circle = Circle('blue')

# - 직접 제거하기
print('Before Delete: ', circle.temp1)
del circle.temp1
#  delattr(circle, 'temp1')
try:
    print('After Delete', circle.temp1)
except AttributeError as e:
    print(e)

# - @prop.deleter 사용해서 삭제
print('Before Delete:', circle.color)
del circle.color

try:
    print('After Delete:', circle.color)
except AttributeError as e:
    print(e)

# - property 자체는 살아있기때문에 재설정가능
circle.color = 'new color'
print(circle.color)
