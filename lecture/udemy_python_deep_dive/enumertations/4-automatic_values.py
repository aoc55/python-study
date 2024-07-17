import enum


# [ enum.auto() 사용 예시 1 ]
class State(enum.Enum):
    WAITING = enum.auto()
    STARTED = enum.auto()
    FINISHED = enum.auto()


print(list(State))
print("------------------------")


# [ enum.auto() 사용 예시 2 ]
class StateV2(enum.Enum):
    WAITING = 100
    STARTED = enum.auto()       # 101
    FINISHED = enum.auto()      # 102


print(list(StateV2))
print("------------------------")

# [ enum.auto() => Anti Pattern ]
try:
    @enum.unique
    class StateV3(enum.Enum):

        # 아래와 같이 혼합사용도 X
        WAITING = enum.auto()
        STARTED = 1
        FINISHED = enum.auto()

    print(list(StateV3))
except Exception as e:
    print(type(e), e)
print("------------------------")


# [ enum.auto() 사용 예시 3 ]
import random
random.seed(0)


class StateV4(enum.Enum):

    def _generate_next_value_(name, start, count, last_values):
        print(f">> _generate_next_value_ {name}, {start}, {count}, {last_values}")
        while True:
            new_value = random.randint(1, 100)
            if new_value not in last_values:
                return new_value

    WAITING = enum.auto()
    STARTED = enum.auto()
    FINISHED = enum.auto()


print(list(StateV4))
print("------------------------")


# [ enum.auto() 사용 예시 4 ]
class StateV5(enum.Enum):

    def _generate_next_value_(name, start, count, last_values):
        return name.title()         # 꼭 정수일 필요 없음

    WAITING = enum.auto()
    STARTED = enum.auto()
    FINISHED = enum.auto()


print(list(StateV5))
print("------------------------")


#  [ Key 값만 필요한 Enum 의 경우 정의 예시 ]
class StateV6(enum.Enum):
    """ Please do not use member values - there are meaningless and subject to change"""
    WAITING = object()
    STARTED = object()
    FINISHED = object()


print(list(StateV6))
print("------------------------")


#  [ Alias 의 경우 Master 와 동일한 값 사용하게 하기 ]
class Aliased(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        print(f">> _generate_next_value_ {name}, {start}, {count}, {last_values}")
        return last_values[-1]


class Color(Aliased):

    RED = object()
    CRIMSON = enum.auto()       # RED 와 동일
    CARMINE = enum.auto()       # RED 와 동일

    BLUE = object()
    AQUAMARINE = enum.auto()    # BLUE 와 동일
    AZURE = enum.auto()         # BLUE 와 동일


print(list(Color))
print(Color.__members__)
