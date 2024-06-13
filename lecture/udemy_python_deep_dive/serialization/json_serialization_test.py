# [ Json Serialization 실습 1 ]
import json
import pprint

d1 = {'a': 100, 'b': 200}

# - 직렬화
dump_str = json.dumps(d1, indent=2)
print(type(dump_str))           # type -> str
print(dump_str)                 # 직렬화된 결과


# - 역직렬화
d2 = json.loads(dump_str)
print(type(d2))                 # type -> dict (obj)
print(d2)                       # 역직렬화된 결과

# - 결과 확인
# - 값은 같지만, Object 자체는 별개
print(d1 == d2)                 # True
print(d1 is d2)                 # False

print("--------------------------------------------")

# [ Json Serialization 실습 2 ]
# - 복잡한 구조의 역직렬화 대상
test_str = '''
{
    "name": "ABC",
    "age": 82,
    "funny" : true,
    "temp" : null,
    "myList" : [
        {
            "key1": "value1-1",
            "key2": "value2-1"
        },
        {
            "key1": "value1-2",
            "key2": "value2-2"
        }
    ]
}
'''
# - 역직렬화 수행
# - 수행 시 JSON 내 type -> 매핑되는 Python Type 으로 변경됨
# - ex. null -> None, true -> True 등
test_dict = json.loads(test_str)
pprint.pprint(test_dict)
# {'age': 82,
#  'funny': True,
#  'myList': [{'key1': 'value1-1', 'key2': 'value2-1'},
#             {'key1': 'value1-2', 'key2': 'value2-2'}],
#  'name': 'ABC',
#  'temp': None}

print("--------------------------------------------")

# [ Json Serialization 실습 3 ]
# - Python 에는 존재하는 Type 이지만 -> JSON 에는 존재하지 않는 Type
# - 기본형 등은 자동으로 변경됨

# - Original -> 'Tuple'
d = {'a': (1, 2, 3)}
print(type(d['a']))             # Tuple

# - 직렬화 수행
ser = json.dumps(d)             # 'Python' Tuple => 'JSON' List

# - 단, 다시 역직렬화 수행 시 List 로 변경됨
dser = json.loads(ser)
print(type(dser['a']))          # List

# - 반대로 json 에는 tuple 개념이 없는데 억지로 로드? 실패
wrong_json = "{'a': (1, 2, 3)}"
try:
    json.loads(wrong_json)
except Exception as e:
    print(e)


print("--------------------------------------------")

# [ Json Serialization 실습 4 ]
# - 기본적으로 직렬화 지원하지 않는 경우 -> 오류 발생

# - 'Decimal'
from decimal import Decimal

try:
    json.dumps({'a': Decimal(10)})
except Exception as e:
    print(e)

# - '실수(Complex)'
try:
    json.dumps({'a': 1 + 1j})
except Exception as e:
    print(e)

# - 'Custom Class'
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

try:
    json.dumps({'a': Person('abc', 10)})
except Exception as e:
    print(e)


print("--------------------------------------------")

# [ Json Serialization 실습 5 ]
# - 기본적으로 직렬화 지원하지 않는 경우 -> 별도의 함수 정의?
# - 단, 후속에서 더 나은방법 사용 예정
class PersonV2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def toJSON(self):
        # return {
        #     'name': self.name,
        #     'age': self.age
        # }
        return vars(self)


print(json.dumps({'john': PersonV2('a', 10).toJSON()}))
