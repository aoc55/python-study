# [ __set_name__ 메서드 실습 1 ]
class ValidStringV1:

    def __set_name__(self, owner_class, property_name):
        print(f'>>> __set_name__: owner={owner_class}, property_name={property_name}')


print("-- class Define Start --")
class PersonV1:

    # 최초 Instnace 화 될때 호출됨!
    # 이 시점에 '__set_name__' 호출
    name = ValidStringV1()
    # __set_name__: owner=<class '__main__.Person'>, property_name=name


print("-- class Define End --")
print("-- Instance 생성 Start --")
PersonV1()                            # 이 시점에는 미호출
print("-- Instance 생성 End --")

print("-----------------------------------------------")


# [ __set_name__ 메서드 실습 2 ]
# - 동일한 Descriptor 에 대해서 여러 곳에서 사용하기
class ValidStringV2:

    def __set_name__(self, owner_class, property_name):
        print(f'>> __set_name__: owner={owner_class}, property_name={property_name}')

        # __set__name__ 을 통해 들어온 각각의 Property Name 저장
        self.property_name = property_name


    # 호출 Test
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        print(f'>> __get__ caleed for property {self.property_name} of instance {instance}')


# 정의 및 __set__name__ 호출 Test
class PersonV2:

    first_name = ValidStringV2()
    # __set_name__: owner=<class '__main__.PersonV2'>, property_name=first_name

    last_name = ValidStringV2()
    # __set_name__: owner=<class '__main__.PersonV2'>, property_name=last_name


# __get__ 호출 Test
print()
p2 = PersonV2()
p2.first_name
p2.last_name


print("-----------------------------------------------")


# [ __set_name__ 메서드 실습 3 ]
# - __set__name__ 을 활용한 Descriptor 활용 에시
class ValidStringV3:

    def __init__(self, min_legnth=None):
        self.min_length = min_legnth

    def __set_name__(self, owner_class, name):

        # property name 저장
        self.property_name = name
        print(f'>> __set_name__: owner={owner_class}, property_name={name}')

    def __set__(self, instance, value):

        # Validation 수행
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a String.')
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f'{self.property_name} must be at least {self.min_length} characters')

        # 통과 시 instance 의 Director 에 값 저장
        key = '_' + self.property_name
        setattr(instance, key, value)

    def __get__(self, instance, owner):
        if instance is None:
            return self

        # 저장해두었던 property name 통해서 값 조회
        key = '_' + self.property_name
        return getattr(instance, key, None)


class PersonV3:
    first_name = ValidStringV3(1)
    last_name = ValidStringV3(2)


p = PersonV3()
print()

# - Validation 로직 동작 확인
try:
    p.first_name = 'Alex'
    p.last_name = 'M'
except ValueError as ex:
    print(ex)
print("")

# - 정상 설정
p.first_name = 'Alex'
p.last_name = 'ABCDE'
print(p.__dict__)
# {'_first_name': 'Alex', '_last_name': 'ABCDE'}
print("")

print(p.first_name)
print(p.last_name)
