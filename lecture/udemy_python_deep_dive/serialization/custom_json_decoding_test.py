import json
from pprint import pprint
from datetime import datetime

# [ Custom JSON Decoding 0 ]

p = '''
{
    "time": {
        "objecttype": "datetime",
        "value": "2018-10-21T09:14:00"
    },
    "message": "created this json String"
}
'''
# - 그냥 읽었을 경우
# - "value": "2018-10-21T09:14:00" -> 일반적인 String 으로 변환
pprint(json.loads(p))
# {'message': 'created this json String',
#  'time': {'objecttype': 'datetime', 'value': '2018-10-21T09:14:00'}}

d = json.loads(p)
for key, value in d.items():
    # - 'objecttype' 같은 스키마 필드를 두어서 이를 해석해서 변환 로직 구현
    if isinstance(value, dict) and "objecttype" in value and value['objecttype'] == 'datetime':
        d[key] = datetime.strptime(value['value'], '%Y-%m-%dT%H:%M:%S')

    # IF type -> fraction 이면 .. .또 구현..
    # IF type -> "xxx" .. -> 귀찮음
    # - 즉, type 별로 일일히 구현 ? 귀찮음

pprint(d)
# {'message': 'created this json String',
#  'time': datetime.datetime(2018, 10, 21, 9, 14)}

print("--------------------------------------------")

# [ Custom JSON Decoding 1 ]
# - 변환함수 정의 후 object_hook 필드에 사용

j = '''
{
    "a": 1,
    "b": 2,
    "c": {
        "c.1": 1,
        "c.2": 2,
        "c.3": {
            "c.3.1": 1,
            "c.3.2": 2
        }
     }
}
'''

# - 호출 테스트용
def custom_decodr(arg):
    print("decoding : ", arg, type(arg))
    return arg

# - 해당 변환함수는 JSON 데이터의 모든 Object(dict) 만날때마다 실행
# - 즉, recurision function
d = json.loads(j, object_hook=custom_decodr)
print(d)
# decoding :  {'c.3.1': 1, 'c.3.2': 2} <class 'dict'>
# decoding :  {'c.1': 1, 'c.2': 2, 'c.3': {'c.3.1': 1, 'c.3.2': 2}} <class 'dict'>
# decoding :  {'a': 1, 'b': 2, 'c': {'c.1': 1, 'c.2': 2, 'c.3': {'c.3.1': 1, 'c.3.2': 2}}} <class 'dict'>




print("--------------------------------------------")

# [ Custom JSON Decoding 2 ]
# - 변환함수 정의 후 object_hook 필드에 사용

p = '''
{
    "time": {
        "objecttype": "datetime",
        "value": "2018-10-21T09:14:00"
    },
    "message": "created this json String"
}
'''

def custom_decodr(arg):
    if 'objecttype' in arg and arg['objecttype'] == 'datetime':
        return datetime.strptime(arg['value'], "%Y-%m-%dT%H:%M:%S")
    # if 다른 Type 필요 시 (ex. Fraction ...)
    else:
        return arg


d = json.loads(p, object_hook=custom_decodr)
print(d)


# - Nested 구조에서도 문제 없음

netsted_p = '''
{
    "times": {
        "created": {
            "objecttype": "datetime",
            "value": "2018-10-21T09:14:00"
         },
         "updated": {
            "objecttype": "datetime",
            "value": "2018-10-21T09:14:00"
         }
    },
    "message": "created this json String"
}
'''

d = json.loads(netsted_p, object_hook=custom_decodr)  # 잘동작
print(d)

print("--------------------------------------------")

# [ Custom JSON Decoding 3 ]
# - JSON 의 Schema 를 알고 있는 경우 Custom 하게 구현 가능

# - 직렬화 & 역직렬화 대상
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    # Decoding 에 맞춰서 Encoding 도 구현!
    def toJSON(self):
        return dict(
            objecttype='person',
            name=self.name,
            age=self.age
        )


d3 = '''
{
    "times": {
        "created": {
            "objecttype": "datetime",
            "value": "2018-10-21T09:14:00"
         },
         "updated": {
            "objecttype": "datetime",
            "value": "2018-10-21T09:14:00"
         }
    },
    "person": {
        "objecttype": "Person",
        "name": "kgh",
        "age": 19
    },
    "message": "created this json String"
}
'''

# - 스키마를 알고 있기때문에 커스텀하게 구현 가능
def custom_decodr(arg):
    if 'objecttype' in arg and arg['objecttype'] == 'datetime':
        return datetime.strptime(arg['value'], "%Y-%m-%dT%H:%M:%S")
    # if 다른 Type 필요 시 (ex. Fraction ...)
    if 'objecttype' in arg and arg['objecttype'] == 'Person':
        return Person(arg['name'], arg['age'])
    else:
        return arg


print(json.loads(d3, object_hook=custom_decodr))



print("--------------------------------------------")

# [ Custom JSON Basic Type Decoding ]
# - Basic Type 에 대해 Custom 하기 편한 Argument 별도 제공

d4 = '''
{
    "data_float": 0.02,
    "date_int": 100,
    "data_const": NaN,
    "data_str": "Python"
}
'''

def custom_float(arg):
    return f'CustomFloat-{arg}'

def custom_int(arg):
    return f'CustomInt-{arg}'


def custom_const_none(arg):
    return 'CustonConst->None'

def object_hook(arg):
    return f'ObjectHooK-{arg}'

print(json.loads(d4, parse_float=custom_float, parse_int=custom_int, parse_constant=custom_const_none, object_hook=object_hook))


# dict -> object Hook
# - 각 데이터 타입 만나면 해당되는 타입 메서드


d5 = '''
{
    "data_float": 0.02,
    "date_int": 100,
    "data_nested" : {
        "data_float2": 0.01,
        "date_int2": 101
    },
    "data_const": NaN,
    "data_str": "Python"
}
'''


print(json.loads(d5, parse_float=custom_float, parse_int=custom_int, parse_constant=custom_const_none, object_hook=object_hook))
