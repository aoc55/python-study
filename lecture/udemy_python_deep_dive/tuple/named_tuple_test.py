# [ Tuple 의 문제점 ]
# - Not Readable
point2D_tuple = (10, 20)
print(point2D_tuple[0], point2D_tuple[1])

# - Tuple 구조 변경 시 Code Break
my_tuple = ('A', 'B')
a, b = my_tuple

# my_tuple = ('1', 'A', 'B')    ----> Tuple 구조 변경
# a, b, = my_tuple              ----> 실행 안됨!


# [ Tuple 대안 ? -> Class ? ]
class Point2DClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D (ClassVer) (x={self.x}, y={self.y})'

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y) if isinstance(other, Point2DClass) else False


point_instance = Point2DClass(10, 20)

# - 장점 -->  Readable !
print('from Class -> ', point_instance.x, point_instance.y)

# - 그러나 Tulple 은 변경 불가능하나, Class 통해서 구현 시 값이 수정 가능
point_instance.x = -999
print(point_instance)


# [ Named Tuple 선언 ]
from collections import namedtuple

# Class 를 선언
# Point2D = namedtuple('Point2D', ('x', 'y'))
# Point2D = namedtuple('Point2D', ['x', 'y'])
# Point2D = namedtuple('Point2D', 'x, y')
Point2D = namedtuple('Point2D', 'x y')

# instance 생성
point2d = Point2D(10, 20)                       # Positional Argument
point2d = Point2D(x=10, y=20)                   # Keyword Argument

print(f'Point2D (NamedTupleVer) (x={point2d.x}, y={point2d.y})')

# - Named Tuple 특성
print(isinstance(point2d, tuple) is True)      # Named Tuple -> 'Tuple'
for e in point2d:                              # Named Tuple -> 'Iterable'
    print(e, end=' / ')
print()

# - Immutable 한 Named Tuple
try:
    point2d.x = -999                            # Named Tuple 값 변경 불가
except AttributeError as e:
    print(e)

# - is , ==
p1 = Point2D(1, 1)
p2 = Point2D(1, 1)
print(p1 is p2)     # False
print(p1 == p2)     # True



# [ Named Tuple 선언2 with 'rename' ]
try:
    Person = namedtuple('Person', 'name, age, _ssn')       # '_ssn' 선언 불가능!
    person = Person('my_name', 19, 'my_ssn')
except ValueError as e:
    print(e)

# - Rename 속성 사용
Person = namedtuple('Person', 'name, age, _ssn', rename=True)
print(Person._fields)   # ('name', 'age', '_2')

person = Person('my_name', 19, 'my_ssn')
print(person)            # Person(name='my_name', age=19, _2='my_ssn')





# [ Named Tuple -> Dict ]
Person = namedtuple('Person', 'name, age, _ssn', rename=True)
person = Person('my_name', 19, 'my_ssn')
person_dict = person._asdict()
print(type(person_dict))
print(person_dict)


# [ Named Tuple - 활용예시 ]
Vector = namedtuple('Vector', 'x, y')
vector1 = Vector(10, 20)
vector2 = Vector(30, 40)

# - dotProduct
result = sum([v[0] * v[1] for v in zip(vector1, vector2)])
print(result)


# [ Named Tuple - DocString ]
# - DocString 기본 값
Point2D = namedtuple('Point2D', 'x y')
print(f'기본 DocString -> {Point2D.__doc__}')         # 기본 DocString -> Point2D(x, y)
print(f'기본 DocString -> {Point2D.x.__doc__}')       # 기본 DocString -> Alias for field number 0
print(f'기본 DocString -> {Point2D.y.__doc__}')       # 기본 DocString -> Alias for field number 1

# - DocString Overriding
Point2D.__doc__ = 'new DocString'
Point2D.x.__doc__ = 'new x DocString'
Point2D.y.__doc__ = 'new y DocString'
print(f'정의한 DocString -> {Point2D.__doc__}')        # 정의한 DocString -> new DocString
print(f'정의한 DocString -> {Point2D.x.__doc__}')      # 정의한 DocString -> new x DocString
print(f'정의한 DocString -> {Point2D.y.__doc__}')      # 정의한 DocString -> new y DocString


# - 동일 원리
def my_func():
    pass


my_func.__doc__ = 'my DocString'
print(f'my_func DocString -> {my_func.__doc__}')        # my_func DocString -> my DocString


# [ Named Tuple - Default Value ]
# - Named Tuple 정의하는데 Default Value 를 설정하고 싶을 때

# - 방법1: Prototype + ._replace method
# -- 단점으로 Instance 생성 시 kwargs 만 가능 (poistional X)
# -- 또한 _replace 부분의 코드가 좀 난해(?) 하다
MyNamedTuple1 = namedtuple('MyNamedTuple1', 'x y z')

my_named_tuple_prototype = MyNamedTuple1(0, 0, 0)                       # Prototype -> 초기값이 0
my_named_tuple_instance = my_named_tuple_prototype._replace(y='888')    # _replace(kwargs) 로 필요한 부분만 변경
print(my_named_tuple_instance)


# - 방법2 : __defaults__ 활용
# -- 장점으로 kwargs, args 모두 가능 및 상대적으로 코드 깔끔
# -- 함수 원리
def my_func2(a1, a2=10, a3=20):
    pass


print(f'Default Value (변경전) {my_func2.__defaults__}')        # (10, 20)

my_func2.__defaults__ = (-8, -9)
print(f'Default Value (변경후) {my_func2.__defaults__}')        # (-8, -9)

# -- NamedTuple 도 동일하게 적용
MyNamedTuple2 = namedtuple('MyNamedTuple2', 'x y z')
# -- NamedTuple 의 __new__ 함수에 대한 __defaults__ 설정
MyNamedTuple2.__new__.__defaults__ = (-1, -1)                   # 뒤에서부터 Default Value 설정 (y, z)
# -- Instnace 생성
my_named_tuple2 = MyNamedTuple2(-9)                             # Positional 기반
print(my_named_tuple2)                                          # MyNamedTuple2(x=-9, y=-1, z=-1)
# -- Instnace 생성2
my_named_tuple2 = MyNamedTuple2(x=-9)                           # Kwargs 기반
print(my_named_tuple2)                                          # MyNamedTuple2(x=-9, y=-1, z=-1)


# [ Named Tuple - Modify ]
# - 기본적으로 Immutable 하기 때문에, 특정 값을 변경하고 싶을 때 방법
# - => 사실 새로운 메모리 공간에 변경된 Tuple 할당됨
MyNamedTuple3 = namedtuple('MyNamedTuple3', 'x y z')
my_named_tuple3_instance1 = MyNamedTuple3(1, 2, 3)

# - [방법1]
# - 신규 Tuple 생성 시 기존 Tuple Value 참고
my_named_tuple3_instance1_2 = MyNamedTuple3(my_named_tuple3_instance1.x, my_named_tuple3_instance1.y, 999)

# - [방법2]
# - 기존 Tuple 의 Value 꺼내서 조작 후, 변경 후 Tuple 생성
# - 그러나 꺼낸 Value 가 길 경우 조작 다소 복잡
value = list(my_named_tuple3_instance1[:-1])
value.append(-777)        # [1, 2, -777]
print(f'Modified Tuple = {MyNamedTuple3(*value)}')
print(f'Modified Tuple = {MyNamedTuple3._make(value)}')

# - [방법3]
# - instance Method 인 '_replace' 사용
my_named_tuple3_instance1_3 = my_named_tuple3_instance1._replace(z=-777)
print(f'Modified Tuple = {my_named_tuple3_instance1_3}')


# [ Named Tuple - Extend ]
# - 기존에 정의한 NamedTuple 을 확장하고 싶을 경우
MyNamedTuple4 = namedtuple('MyNamedTuple4', 'x, y')

# - 기존 tuple 의 '_fields' 필드 사용
new_fields = MyNamedTuple4._fields + ('z', )
MyNamedTuple4Extended = namedtuple('MyNamedTuple4Extended', new_fields)
print(f'Extended Tuple = {MyNamedTuple4Extended(x=1, y=2, z=3)}')

# - 더 짧게?
MyNamedTuple4Extended2 = namedtuple('MyNamedTuple4Extended2', MyNamedTuple4._fields + ('z', ))
print(f'Extended Tuple 2 = {MyNamedTuple4Extended2(x=1, y=2, z=3)}')

# 확장된 Tuple 에 기존 Tuple의 Instance 값도 넣기
my_named_tuple4_instance1 = MyNamedTuple4('1', '2')

my_named_tuple4_extended_instance1 = MyNamedTuple4Extended(*my_named_tuple4_instance1 + ('3', ))
print(f'Extended Tuple Instance = {my_named_tuple4_extended_instance1}')

my_named_tuple4_extended_instance2 = MyNamedTuple4Extended._make(my_named_tuple4_instance1 + ('3', ))
print(f'Extended Tuple Instance2 = {my_named_tuple4_extended_instance2}')

