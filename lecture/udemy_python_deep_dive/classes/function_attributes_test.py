class PersonV0:
    def set_name():
        pass

# <function PersonV0.set_name at 0x10296c040>
print(PersonV0.set_name)


p0 = PersonV0()
# <bound method PersonV0.set_name of <__main__.PersonV0 object at 0x102987fa0>>
print(p0.set_name)

try:
    p0.set_name()
except TypeError as e:
    print(e)
    # set_name() takes 0 positional arguments but 1 was given

print("------------------------")

# [ 첫번재 인자로 Instance 받기]
class PersonV1:
    def set_name(instance_obj, new_name):
        instance_obj.name = new_name


p1 = PersonV1()
p1.set_name('hi')
print(p1.__dict__)


print("------------------------")

# [ 관용적 표현인 'Self' 사용 ]
class PersonV2:
    def say_hello(self):
        print("hello~")
    def set_name(self, new_name):
        self.name = new_name


p2 = PersonV2()
p2.set_name('hi')
print(p2.__dict__)

print("------------------------")

# - Function vs Bounded Method 비교
print(PersonV2.say_hello, p2.say_hello)

# - Bounded Method 의 특성 파악
m_hello = p2.say_hello
print(m_hello.__func__, m_hello.__self__)
m_hello.__func__(p2)


print("-----------------------------")

# [ 동적으로 Class 에 Function 추가 시 Bounded method 동적 추가(?) ]
class PersonV3:
    def say_hello(self):
        print("hello~")


p3 = PersonV3()         # 인스턴스 먼저 생성

PersonV3.other_func = lambda self: print("other func~")     # 동적으로 Class 에 Function 추가

print(p3.other_func)    # 인스턴스에 관련된 Bounded Method 생성됨


# [ MethodType 을 통해 Runtime 에 Instnace 에 Function Attribute 추가하기 ]
class Person:
    def __init__(self, name):
        self.name = name


p1 = Person('abc')


# - 일반 function 매핑?
p1.say_hello = lambda: print('~ hello ~')
print(p1.say_hello)     # {'say_hello': <function <lambda> at 0x10524f160>}
# - function 이지 bound method 아님 -> instance ns 접근 불가
p1.say_hello()
print("")

# - MethodType 기반의 Bound Method 생성
from types import MethodType
p2 = Person('zzz')


# - 등록할 함수 -> instance namespace 접근 기반 (self)
def say_hello(self):
    return print(f'"{self.name}" says hello')


# - MethodType 으로 변환 후 매핑
p2_say_hello = MethodType(say_hello, p2)
p2.say_hello = p2_say_hello
print(p2.say_hello)
print(p2.__dict__)
p2.say_hello()
print("")

# - Lambda 기반으로 MethodType 생성하기
p2.test_print = MethodType(lambda self: print("test-print"), p2)
p2.test_print()
print("")

# - MethodType 생성 및 매핑의 경우 Instance 단위로만 적용
print(p1.__dict__)
print(p2.__dict__)

print("-----------------------------")

# [ MethodType 을 활용한 다형성(?) 등 예시 ]

class Teacher:
    def __init__(self, name):
        self.name = name

    # func 를 입력 받아서 MethodType 으로 바운딩 후 Attribute 로 저장
    def register_do_work(self, func):
        setattr(self, '_do_work', MethodType(func, self))
        # self._do_work = MethodType(func, self)

    # 저장한 Method Attribute 호출
    def do_work(self):
        do_work_method = getattr(self, '_do_work', None)        # 예외처리(None 리턴)를 위한 getattr 사용
        # do_work_method = self._do_work
        if do_work_method:
            return do_work_method()
        else:
            raise AttributeError('Not Registered Method')


math_teacher = Teacher('math_Teacher')
math_teacher.register_do_work(lambda self: print(f'{self.name} -> teach math!!!!'))
print(math_teacher.__dict__)
print("")

english_teacher = Teacher('english Teacher')
english_teacher.register_do_work(lambda self: print(f'{self.name} -> teach English!!'))
print(english_teacher.__dict__)
print("")

# - 다형성 기반 호출?
for teacher in [math_teacher, english_teacher]:
    teacher.do_work()

