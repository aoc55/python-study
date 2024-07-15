# [ Property Lookup Resolution (1) ]
# - Data Descritor VS Non Data Descritpor 에 따라 다르게 동작

# - (1) Data Descriptor
class IntegerValue:

    def __set__(self, instance, value):             # __set__ 구현
        print(" >> IntegerValue's __set__ called !!")
        pass

    def __get__(self, instance, owner_class):
        print(" >> IntegerValue's __get__ called !!")
        pass


class Point:
    x = IntegerValue()


p = Point()

# - Data Descriptor 임으로 Instance Dict 가 아닌, Descriptor 통하게 됨!
p.x = 10        # __set__
print(p.x)      # __get__

# {} -> Instance Dict 는 비어있음
print(p.__dict__)


print("-----------------------------------------------")

# [ Property Lookup Resolution (2) ]

# - (2) Non Data Descriptor
class TimeUTC:

    def __get__(self, instance, owner):
        print("  >> TimeUTC's __get__ called !!")

    # __set__ 미구현


class Logger:
    current_time = TimeUTC()

# - (Non Data) Descriptor 임으로 get의 경우 Instance Dict 가 아닌, Descriptor 통하게 됨!
l = Logger()
print(l.current_time)
print("")

# - Non Data Descriptor 임으로 set의 경우 Instance Dict 가 아닌, Descriptor 통하게 됨!
l.current_time = 123
print(l.current_time)   # 123
print(l.__dict__)       # {'current_time': 123}
print("")

# - instance's Dict 내 Attribute 삭제
del l.current_time
print("(del l.current_time)")
print("")

# - 이후 조회는 다시 Descriptor 통해서 수행
print(l.current_time)
print()


print("-----------------------------------------------")

# [ Property Lookup Resolution (3) ]

class ValidString:

    def __init__(self, min_legnth=None):
        self.min_length = min_legnth

    def __set_name__(self, owner_class, name):
        self.property_name = name

    def __set__(self, instance, value):

        print(f"  >> __set__ called {instance}, {self.property_name}")

        # Validation 수행
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a String.')
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f'{self.property_name} must be at least {self.min_length} characters')

        # 만약 property_name을 key 를 그대로 사용할 경우
        # setattr(instance, self.property_name, value) => 사용 시 무한 Recursive 걸릴 수 있음
        # 따라서 '__dict__'에 값 직접 매핑
        instance.__dict__[self.property_name] = value


    def __get__(self, instance, owner):

        print(f"  >> __get__ called {instance}, {self.property_name}")

        if instance is None:
            return self

        # 만약 property_name을 key 를 그대로 사용할 경우
        # return getattr(instance, self.property_name, None) => 사용 시 무한 Recursive 걸릴 수 있음
        return instance.__dict__.get(self.property_name, None)


class Person:
    first_name = ValidString(1)
    last_name = ValidString(1)


p = Person()
p.first_name = 'ok'     # __set__
print(p.first_name)     # __get__