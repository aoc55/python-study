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
    Person = namedtuple('Person', 'name, age, _ssn')       # 선언 불가능!
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


# [ Named Tuple 활용예시 ]
Vector = namedtuple('Vector', 'x, y')
vector1 = Vector(10, 20)
vector2 = Vector(30, 40)

# - dotProduct
result = sum([v[0] * v[1] for v in zip(vector1, vector2)])
print(result)

