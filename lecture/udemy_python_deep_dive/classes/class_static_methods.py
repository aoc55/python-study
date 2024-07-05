# [ Class & Static Method ]
class MyClass:

    # Regular Function ?
    def hello():
        print("hello")

    # instnace Method
    def instance_hello(self):
        print(f'hello from {self}')

    # class Method
    # - always bound to the class
    @classmethod
    def class_hello(cls):
        print(f'hello form {cls}')

    # static Method
    @staticmethod
    def static_hello():
        print("static Method Called")


# [Regular Method] 호출
# - Class Level 에서 호출
print("--Class--")
print(MyClass.hello)        # regular Method !! <function MyClass.hello at 0x100f20ee0>
MyClass.hello()

# - Instance Level 에서 호출
print("--Instance--")
m = MyClass()
print(m.hello)              # <bound method MyClass.hello of <__main__.MyClass object at 0x100f2edc0>>
try:
    m.hello()               # Instance 에 바운드됨!!
except TypeError as e:      # TypeError Exception 발생
    print(e)                # Bounded 된 메서드 호출 시 첫번째 Argument 로 본인 object Injection 함

print("------------------------")

# [Instnace Method 호출]
print("--Class--")
print(MyClass.instance_hello)   # regular Method !! -> <function MyClass.instance_hello at 0x104f03040>
MyClass.instance_hello('temp')  # 돌아는 가지만 정상적이지 않음

print("--Instance--")
print(m.instance_hello)         # Instance 에 바운드됨!! -> <bound method MyClass.instance_hello of <__main__.MyClass object at 0x104f06dc0>>
m.instance_hello()

print("------------------------")

# [Class Method 호출]
# - 항상 Class 에 Bound 됨
print("--Class--")
print(MyClass.class_hello)       # Class 에 바운드됨!! -> <bound method MyClass.class_hello of <class '__main__.MyClass'>>
MyClass.class_hello()

print("--Instance--")
print(m.class_hello)             # Class 에 바운드됨!! -> <bound method MyClass.class_hello of <class '__main__.MyClass'>>
m.class_hello()


print("------------------------")
# [Static method 호출]
print("--Class--")  
print(MyClass.static_hello)     # regular Method !! -> <function MyClass.static_hello at 0x104f03160>
MyClass.static_hello()

print("--Instance--")
# - Class -> Static Method
print(m.static_hello)           # regular Method !! -> <function MyClass.static_hello at 0x104f03160>
m.static_hello()

print("------------------------")

# [ Class Method 활용 예시 ]
from datetime import datetime, timezone, timedelta


class CustomTimeError(Exception):
    """A custom Exception Used For Timer Class"""       # 이것도 코드임,
                                                        # 따라서 별도의 pass 등 안써도 됨


class CustomTimer:

    tz = timezone.utc                                       # Class Attribute

    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)    # Class Attribute 변경처리

    @classmethod
    def current_dt(cls):
        return datetime.now(cls.tz)                         # Class Attribute 기반한 동작

    @staticmethod
    def current_dt_utc():                                   # Class, Instance 랑 상관 X
        return datetime.now(timezone.utc)

    # Instance Method
    def start(self):
        self._time_start = self.current_dt_utc()            # Instance Attribute 조작
        self._time_end = None

    def stop(self):                                         # Instance Attribute 조작
        if self._time_start is None:
            raise CustomTimeError("Start 먼저 호출 필요")
        self._time_end = self.current_dt_utc()

    # 시간 추출용 프로퍼티 설정
    # - 리턴 시 클래스의 현재 tz 에 맞춰 리턴
    @property
    def start_time(self):
        if self._time_start is None:
            raise CustomTimeError("Timer not Started")
        return self._time_start.astimezone(self.tz)

    @property
    def end_time(self):
        if self._time_end is None:
            raise TimeoutError('Timer Not Stopped')
        return self._time_end.astimezone(self.tz)

    @property
    def elapsed_time(self):
        if self._time_start is None:
            raise CustomTimeError("Timer not Started")
        if self._time_end is None:
            elapsed_time = self.current_dt_utc() - self._time_start
        else:
            elapsed_time = self._time_end - self._time_start

        return elapsed_time.total_seconds()


# - 메소드 호출 테스트
t1 = CustomTimer()
t2 = CustomTimer()

# - Static Method 호출
print(t1.current_dt_utc(), t2.current_dt_utc())


# - Class Method 통한 Class Attribute 조정
print('Before ->', CustomTimer.tz, t1.tz, t2.tz)
t2.set_tz(-7, 'MST')
print('After ->', CustomTimer.tz, t1.tz, t2.tz)

# - 참고 -> Class Attribute 위치
print(CustomTimer.__dict__)
print(t1.__dict__, t2.__dict__)

print("-------------------------------")

# - 활용 테스트
from time import sleep

my_timer_1 = CustomTimer()
my_timer_1.start()
sleep(2)
my_timer_1.stop()
print(f'Start Time {my_timer_1.start_time}')
print(f'End Time {my_timer_1.end_time}')
print(f'Elapsed {my_timer_1.elapsed_time} seconds')

# Class Attribute 변환
t2.set_tz(-7, 'MST')

my_timer_2 = CustomTimer()
my_timer_2.start()
sleep(2)
my_timer_2.stop()
print(f'Start Time {my_timer_2.start_time}')
print(f'End Time {my_timer_2.end_time}')
print(f'Elapsed {my_timer_2.elapsed_time} seconds')
