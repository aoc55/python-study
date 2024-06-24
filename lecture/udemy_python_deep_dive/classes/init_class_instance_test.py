# [ Instance Init 호출 시점 ]
class Person:
    def __init__(self):
        print(f'Initializing a new Person Object : {self}')     # 이 시점에 이미 instnace 있음 (메모리 주소)


# - init 호출 시점은 Instnace 객체 실제 생성 이후임
p = Person()
print(hex(id(p)))


print("-----------------------------")


# [ Instance Init 호출 원리 ]
class PersonV2:
    def custom_init(self, name):
        self.name = name

    def __repr__(self):
        return f'PersonV2(name={self.name})'


p2 = PersonV2()         # instance 생성
p2.custom_init('kgh')   # 이후 init 함수 호출
print(p2)


p3 = PersonV2()
# - 실제 init 호출 원리
PersonV2.custom_init(p3, 'kgh2')
print(p3)
