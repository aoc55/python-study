# [ Delegating to Parent 실습 1 ]
class Person:
    def work(self):
        return "Person works ... "


class Student(Person):
    pass


class PythonStudent(Student):
    def work(self):
        # - (1) 직전 부모에 없어도, 부모의 부모 등 .. 상위로 올라가면서 탐색함
        # - (2) 오버라이딩 했으므로, 부모의 메서드를 명시적으로 부르기 위해 super(). 사용
        result = super().work()
        return f'Python Student works .... and {result}'


ps1 = PythonStudent()
print(ps1.work())

print("------------------------------------")


# [ Delegating to Parent 실습 2 ]
class Person:
    def work(self):
        return "Person works ... "


class Student(Person):
    def study(self):
        return "Student Studies ... "


class PythonStudent(Student):
    def code(self):

        # - (1) 오버라이딩 한게 아니라면 굳이 super() 부를 필요 없음
        # - (2) self.XXX 로 불러도 됨
        result_1 = self.work()
        result_2 = self.study()
        return f'{result_1} and {result_2} and PythonStudent codes .... '


ps1 = PythonStudent()
print(ps1.code())

print("------------------------------------")


# [ Delegating to Parent 실습 3 ]
# - 가장 흔히 Delegate To Parent 되는 __init__ 예시
class Person:
    def __init__(self, value):
        print("Init Name Using Person's __init__ Method .... ")
        self.name = value


class Student(Person):
    def __init__(self, name, student_number):
        super().__init__(name)
        self.student_number = student_number


s = Student('KGH', 10)

# - super() 통해서 호출 했지만 실제로 지정된건 현재 '인스턴스'의 dir
# - 왜냐하면 -> 해당 메서드는 상위클래스에 있지만, 현재 인스턴스에 Bound 되어 있으므로
print(s.__dict__)                       # {'name': 'KGH', 'student_number': 10}
print('name' in s.__dict__)             # True
print('student_number' in s.__dict__)


print("------------------------------------")


# [ Delegating to Parent 실습 3 ]
# - __init__ 메서드 별도로 미 구현시 부모 클래스의 __init__ 메서드 사용
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    pass

try:
    s1 = Student()
except TypeError as e:
    print(e)            # __init__() missing 1 required positional argument: 'name'

print(Student.__init__ is Person.__init__)  # True

print("------------------------------------")


# [ Delegating to Parent 실습 4 ]
# - 예시 클래스 생성

from math import pi
from numbers import Real


# - 부모 클래스 정의
class Circle:
    def __init__(self, r):
        print("-->> init 호출 .. ")
        self.radius = r             # property Setter 호출됨
        self._area = None
        self._perimeter = None

    @property
    def radius(self):
        return self._r

    @radius.setter
    def radius(self, r):
        print("-->> radis.setter 호출..")
        if isinstance(r, Real) and r > 0:
            self._r = r
            self._area = None
            self._perimeter = None
        else:
            raise ValueError("radius must be a positive real number")

    @property
    def area(self):
        if self._area is None:
            self._area = pi * self.radius ** 2
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = 2 * pi * self.radius
        return self._perimeter


# - **성공케이스**
# - 자식 클래스 정의
class UnitCircle(Circle):
    def __init__(self):
        super().__init__(1)


u = UnitCircle()
print(u.radius, u.area, u.perimeter)        # (부모 클래스에 정의된) property 통해서 접근
u.radius = 10                               # (부모 클래스에 정의된) property 통해서 세팅


# - **실패 케이스**
# - 자식 클래스 정의
class UnitCircle(Circle):
    def __init__(self):
        super().__init__(1)

    # - 여기서 자식 클래스에서 property 새로 정의해버림 (오버라이딩)
    # - 이때 setter 는 구현하지 않음
    @property
    def radius(self):
        return super().radius


try:
    u = UnitCircle()
    # - (1) __init__ 호출
    # - (2) (자식에 미정의) 부모 __init__ 호출
    # - (3) __init__ 내 'radius' 프로퍼티의 setter 호출
    # - (4) 자식 클래스 'radius' 프로퍼티 오버라이딩 했으나, setter 미구현
    # - (5) 따라서 오류 발생
except AttributeError as e:
    print(e)            # can't set attribute


print("------------------------------------")


# [ Delegating to Parent 실습 4 ]
# - 위 버전의 개선판?


class CircleV2:
    def __init__(self, r):
        print("-->> init 호출 .. ")
        self._set_radius(r)            # 메서드 호출로 변경
        self._area = None
        self._perimeter = None

    @property
    def radius(self):
        return self._r

    @radius.setter
    def radius(self, r):
        print("-->> radis.setter 호출..")
        self._set_radius(r)

    def _set_radius(self, r):
        print("-->> _set_radius 호출..")
        if isinstance(r, Real) and r > 0:
            self._r = r
            self._area = None
            self._perimeter = None
        else:
            raise ValueError("radius must be a positive real number")

    @property
    def area(self):
        if self._area is None:
            self._area = pi * self.radius ** 2
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = 2 * pi * self.radius
        return self._perimeter


class UnitCircleV2(CircleV2):
    def __init__(self):
        super().__init__(1)


u_v2 = UnitCircleV2()
u_v2._set_radius(10)
print(u_v2.radius)
