# [ Custom Json Encoding 실습 1 ]
# - Python 에서 기본적으로 Serialization 안되는 경우
import json
from _datetime import datetime

# - DateTime type 의 객체 생성
current = datetime.utcnow()
print(current)

# - Serializaiton 시도 ?
try:
    json.dumps(current, indent=2)
except TypeError as e:      # 예외 발생 (Python 이 기본적으로 불가)
    print(e)

# - 데이터 타입에서 직접 JSON 변환에 맞도록 직접 메서드를 호출?
# - (여기서는 .isoformat())
log_record = {
    'time': datetime.utcnow().isoformat(),          # 정상수행됨
    'message': 'testing'
}
print(json.dumps(log_record, indent=2))             # 정상수행됨

print("--------------------------------------------")

# [ Custom Json Encoding 실습 2 ]
# - `json.dumps()` 함수 내 default 파라미터 활용

log_record = {
    'time': datetime.utcnow(),
    'message': 'testing'
}


# - defualt 함수 정의
def my_format_iso(dt):
    return dt.strftime('%Y-%m-%d%T%H:%M:%S')


print(json.dumps(log_record, default=my_format_iso))


# - 그러나 정의한 함수에서 처리 가능한 Type 이 아닌 경우에는 ? 오류 발생!
# - ex. 위 함수는 dateTime 에 대한 함수로 정의했는데, 'Set' Type 이 인자로 전달되면?
log_record2 = {
    'time': datetime.utcnow(),
    'message': 'testing',
    'args': {1, 2, 3}       # set 부여
}

try:
    print(json.dumps(log_record2, default=my_format_iso))       # default 로 전달되는 함수 실행 중 오류 발생
except Exception as e:
    print(e)


print("--------------------------------------------")


# [ Custom Json Encoding 실습 3 ]
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.created_dt = datetime.utcnow()

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def toJSON(self):
        # return {
        #     'name': self.name,
        #     'age': self.age,
        #     'created_dt': self.created_dt.isoformat()
        # }
        #
        return vars(self)


# - default 파라미터로 전달되는 함수에 대해서 여러 Type 이 와도 처리가 가능하게 구현하기
def custom_json_formatter(arg):
    # dateTime, set, person ... 등 처리 가능하도록 구현
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)
    elif isinstance(arg, Person):
        return arg.toJSON()


# - Custom Formatter 사용
p = Person('kgh', 19)
print(json.dumps(p, default=custom_json_formatter))


print("--------------------------------------------")


# [ Custom Json Encoding 실습 4 ]
# - '별도의 JSON Type 으로 출력함수를 정의하지 않은 Custom Class 도 대비하기'

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

    # toJson 구현 X


# - Custom Formatter 정의
def custom_json_formatter_v2(arg):
    if isinstance(arg, datetime):       # dt
        return arg.isoformat()
    elif isinstance(arg, set):          # set
        return list(arg)
    else:
        try:
            return arg.toJSON()         # toJSON
        except AttributeError:
            try:
                return vars(arg)
            except TypeError:
                return str(arg)


from decimal import Decimal


point = Point(10, 10)
print(json.dumps(point, default=custom_json_formatter_v2))

point2 = Point(Decimal(10), Decimal(10))
print(json.dumps(point2, default=custom_json_formatter_v2))

person2 = Person('jONH', 18)
print(json.dumps(person2, default=custom_json_formatter_v2))


# - Nested 구조에서도 가능
log_record = dict(
    time=datetime.utcnow(),                  # dt
    message='Created New Point',             # String
    point_1=point,                           # Custom Class
    point_2=point2,                          # Custom Class
    created_by=person2                       # Custom Class
)


print(json.dumps(log_record, default=custom_json_formatter_v2))

# 그러나 .... 매번 타입마다 하나의 메서드에 일일히 매번 IF 문 추가..? -> tedious (귀찮음)

print("--------------------------------------------")


# [ Custom Json Encoding 실습 5 ]
# - 일일히 하나의 함수에 분기처리 하는 것이 아닌 @singledispatch 데코레이터 활용
from functools import singledispatch
from fractions import Fraction

# - Base 함수 생성
# - 별도에서 빠지지 않을 경우 수행됨
@singledispatch
def json_format(arg):
    print(arg)
    try:
        return arg.toJSON()
    except AttributeError:
        print('>>>>>> fail arg.toJSON()')
        try:
            return vars(arg)
        except TypeError:
            print('>>>>>> fail vars(arg)')
            return str(arg)


# - Type 별로 정의
# - Data Type 에 맞게 수행
@json_format.register(datetime)
def _(arg):
    print(">> dt json_format 수행")
    return arg.isoformat()


@json_format.register(set)
def _(arg):
    print(">> dt json_format 수행")
    return list(arg)


print("--------------------------------------------")


# - 다시 호출 테스트
log_record = dict(
    time=datetime.utcnow(),
    message='Created New Point',
    point=point,
    created_by=p
)

print(json.dumps(log_record, indent=2, default=json_format))

print("--------------------------------------------")


# - 호출테스트 2번째
@json_format.register(Decimal)      # - 데이터 타입 필요에 따라 타입에 따른 포맷터 추가
def _(arg):
    return f'Custom Decimal(str({arg}))'


d = dict(
    a=1+1j,
    b=Decimal('0.5'),
    c=Fraction(1, 3)
)

print(json.dumps(d, indent=2, default=json_format))

