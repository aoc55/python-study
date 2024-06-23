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


print("------------------------")

# [ 동적으로 Class 에 Function 추가 시 Bounded method 동적 추가(?) ]
class PersonV3:
    def say_hello(self):
        print("hello~")


p3 = PersonV3()         # 인스턴스 먼저 생성

PersonV3.other_func = lambda self: print("other func~")     # 동적으로 Class 에 Function 추가

print(p3.other_func)    # 인스턴스에 관련된 Bounded Method 생성됨




