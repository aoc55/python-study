# [1]
# 기본적인 Class 정의 및 매직메서드 활용
class MyClass1:                     # Class Name은 Camel 표기법
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("[__init__] called")

    def __str__(self):
        return f'MyClass1 -> {self.x} and {self.y}'

    def __repr__(self):
        return f'MyClass1({self.x}, {self.y})'


# [2]
# Protected Field 실습
class MyClass2:
    def __init__(self, x):
        self._hidden_x = x          # _로 시작하면 Protected 필드


# [3]
# 명시적인 set_, get_ 구현
# 그러나
# 1. 파이써닉하지 않고,
# 2. 정의한 set_이 아닌 직접 value 에 접근하는 걸 막을 수는 없음 (이게 당연한 거임)
class MyClass3:
    def __init__(self, value):

        if value < 0:
            raise ValueError("ValueError:: Must Value >= 0")

        self._value = value

    def get_value(self):
        print("[get_value] called")
        return self._value

    def set_value(self, value):     # Set 구문에 로직을 추가하고 싶을때
        print("[set_value] called")

        if value < 0:
            raise ValueError("ValueError:: Must Value >= 0")

        self._value = value


# [4]
# Decorator 통한 setter, getter 구현
# 1. _value 식으로 Field 정의
# 2. @property, @value.setter 데코레이터를 통해 getter, setter 구현
# 3. 내부 참조에서도 데코레이터 통하거나 직접 필드 통하거나
class MyClass4:
    def __init__(self, value):
        if value < 0:
            raise ValueError("ValueError:: Must Value >= 0")
        self._value = value

    @property                                   # Getter Decorator 구현
    def value(self):
        print("[Value] @property Called")
        return self._value

    @value.setter                               # Setter Decorator 구현
    def value(self, value):
        print("[set_value] @value.setter Called")

        if value < 0:
            raise ValueError("ValueError:: Must Value >= 0")

        self._value = value

    def test_func1(self):
        return f'test_func1 => {self.value}'    # 내부 접근도 Decorater 통해서 접근하기

    def test_func2(self):
        return f'test_func2 => {self._value}'   # 내부 접근 시 아니면 Prorpety 직접 접근하기


if __name__ == "__main__":

    # [1]
    my_class_1 = MyClass1(10, 20)
    print(my_class_1)
    print("-----------------")

    # [2]
    my_class_2 = MyClass2(999)
    # Proteceted 필드 접근
    print(my_class_2._hidden_x)      # IDE 에서 경고는 뜨나 파이썬에서 정상실행됨
    print("-----------------")

    # [3]
    try:
        my_class_3 = MyClass3(-999)
    except ValueError as ve:
        print(ve)

    try:
        my_class_3 = MyClass3(1)
        my_class_3.set_value(-999)  # 정의한 명시적 setter 로직에 따라 ValueError 발생
    except ValueError as ve:
        print(ve)

    my_class_3 = MyClass3(1)
    my_class_3._value = -999        # 하지만 Proctected Field 에 대한 Dircet Access 는 막을 수 없음 (몽키패치?)
    print(my_class_3.get_value())
    print("-----------------")

    # [4]
    my_class_4 = MyClass4(1)
    try:
        my_class_4.value = -999     # Decorator 통해서 구현한 setter 에 의해 Error 발생
    except ValueError as ve:
        print(ve)

    my_class_4.value = 777
    print(my_class_4.value)         # Decorator 통해서 구현한 Getter 에 의해 값 가져옴 (실제 저장은 _value field)
    print(my_class_4.test_func1())
    print(my_class_4.test_func2())