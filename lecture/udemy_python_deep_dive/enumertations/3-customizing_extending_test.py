from enum import Enum


# [ Enum Customizing 예시 1 ]
class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3

    # - 필요한 Magic Method 구현
    def __str__(self):
        return f'[{self.name} -> {self.value}]'

    def __lt__(self, other):
        return isinstance(other, Number) and self.value < other.value


print(Number.ONE)
print(Number.ONE < Number.TWO)
print(Number.ONE == Number.TWO)
print("------------------------")


# [ Enum Customizing 예시 2 ]
class Phase(Enum):
    READY = 'ready'
    RUNNING = 'running'
    FINISHED = 'finished'

    def __str__(self):
        return self.value

    def __eq__(self, other):
        if isinstance(other, Phase):
            return self is other
        elif isinstance(other, str):
            return self.value == other
        return False

    # - str 기반의 lt 구현 (참고만...
    def __lt__(self, other):

        ordered_items = list(Phase)
        self_order_index = ordered_items.index(self)

        if isinstance(other, Phase):
            other_order_index = ordered_items.index(other)
            return self_order_index < other_order_index

        if isinstance(other, str):
            try:
                other_member = Phase(other)
                other_order_index = ordered_items.index(other_member)
                return self_order_index < other_order_index
            except ValueError as e:
                print(e)
                return False


print(Phase.READY == 'ready')
print(Phase.READY < Phase.RUNNING)
print(Phase.READY < 'running')
print("------------------------")


# [ Enum Extend 예시 1 ]
class ColorBase(Enum):

    # method 만 정의한 경우 상속 가능
    def hello(self):
        return f'{str(self)} says Hello~'


# - Extend
class Color(ColorBase):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


print(Color.RED.hello())
print("------------------------")


# [ 기존 Enumeration 예시 ]
from http import HTTPStatus
print(type(HTTPStatus))
print(list(HTTPStatus)[0:10])
print(HTTPStatus.CREATED.name, HTTPStatus.CREATED.value)
print("------------------------")


# [ Enum Customizing 예시 3 ]
# - property 적용
class AppStatus(Enum):
    OK = (0, 'No Problem!')
    FAILED = (1, 'Crap !')

    @property
    def code(self):
        return self.value[0]

    @property
    def phase(self):
        return self.value[1]


print(AppStatus.FAILED.name, AppStatus.FAILED.value)
print(AppStatus.FAILED.code)
print(AppStatus.FAILED.phase)
print("------------------------")


# [ Enum Customizing 예시 4 ]
# - 상위 클래스에서 인스턴스화 메서드 호출
class TwoValueEnum(Enum):

    def __new__(cls, member_value, member_phrase):
        print(f' >> called __new__ {member_value}, {member_phrase}')
        member = object.__new__(cls)

        member._value_ = member_value
        member.phrase = member_phrase

        return member


class AppStatusV2(TwoValueEnum):
    OK = (0, 'No Problem!')         # instance 생성 -> 상위에 정의한 __new__ 호출
    FAILED = (1, 'Crap!')           # instance 생성 -> 상위에 정의한 __new__ 호출


print(AppStatusV2.FAILED)
print(AppStatusV2.FAILED.name, AppStatusV2.FAILED.value)
print(AppStatusV2.FAILED.phrase)
