# [ Descriptor __get__ 분석 ]
from datetime import datetime


class TimeUTC:  # Descriptor 정의

    def __get__(self, instance, owner):
        print(f'__get__ called, self={self}, instance={instance}, owner_clazz={owner}')
        return datetime.utcnow().isoformat()


# Descriptor 활용
class Logger1:
    current_time = TimeUTC()


class Logger2:
    current_time = TimeUTC()


print(Logger1.current_time)     # - Class 에서 호출
print(Logger1().current_time)   # - Instnace 에서 호출
print()

print(Logger2.current_time)     # - Class 에서 호출
print(Logger2().current_time)   # - Instnace 에서 호출
print("-------------------------------------")


# [ Descriptor -> __get__ 구현 ]
class TimeUTC:

    # 아래와 같이 구현이 사실상 표준
    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            print(f'__get__ called, self={self}, instance={instance}, owner_clazz={owner}')
            return datetime.utcnow().isoformat()


class Logger:
    current_time = TimeUTC()


print("from Class => ", Logger.current_time)          # - Class 에서 호출
print("from Instance => ", Logger().current_time)        # - Instnace 에서 호출
print("-------------------------------------")


# [ 참고 - Property Ver 도 동일하게 구현되어 있음 ]
class Logger:

    @property
    def current_time(self):
        return datetime.utcnow().isoformat()


print("from Class => ", Logger.current_time)
print("from Instance => ", Logger().current_time)
# from Class =>  <property object at 0x100cf2860>
# from Instance =>  2024-07-10T07:53:35.023267
print("-------------------------------------")


# [ 주의사항 - Descriptor 인스턴스에서 state 가지고 있을 경우 ]
class Countdown:
    def __init__(self, start):
        self.start = start + 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        self.start -= 1
        return self.start


class Rocket:
    countdown = Countdown(10)


# 여러 클래스의 인스턴스에서 "동일한 Descriptor 인스턴스" 사용
rocket1 = Rocket()
rocket2 = Rocket()

print(rocket1.countdown)
print(rocket1.countdown)

# - Rokect 2
# - Countdown 인스턴스 공유로 인한 문제
print(rocket2.countdown)        # 8
print("-------------------------------------")


# [ Descriptor __set__ 구현 시 문제점 2 ]
class IntegerValue:

    def __set__(self, instance, value):
        self._value = value     # 역시 descriptor 자체에 state 보유

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return self._value


class Point2D:
    x = IntegerValue()
    y = IntegerValue()


p1 = Point2D()
p1.x = 10
p1.y = 20

p2 = Point2D()
p2.x = 100
p2.y = 200

print(p1.x)         # 100으로 바뀌어버림

