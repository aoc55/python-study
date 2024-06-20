from numbers import Real

# [ 직접 클래스 구현 ]
# - (결론) 사실상 실용성 없음
class IntDict:

    def __init__(self):
        self._d = {}        # 내부에서 Dictionary 가지고 있기?

    def __setitem__(self, key, value):
        if not isinstance(value, Real):
            raise ValueError("Value must be a real number")
        self._d[key] = value

    def __getitem__(self, key):
        return int(self._d[key])


d = IntDict()

# - 아래는 직접 구현한 정상 '매직메서드' 통해서 사용 가능
d['a'] = 10.5
print(d['a'])

# - 그러나 아래와 같은 메소드들을 일일히 구현하지 않으면 불가
# - 'Lost a lot of functionality'
try:
    d.get('a')
except AttributeError as e:
    print(e)

print("-------------------------------")


# [ 'dict' 클래스 상속을 통한 구현 Ver ]
class IntDictV2(dict):          # 상속
    def __setitem__(self, key, value):

        # 커스텀 로직
        if not isinstance(value, Real):
            raise ValueError('Value Must Be a Real Number')

        # 이후 dict 의 매직메서드 호출
        super().__setitem__(key, value)

    def __getitem__(self, key):

        # dict 의 매직메서드 기반에 커스텀 로직 추가
        return int(super().__getitem__(key))


d2 = IntDictV2()

# - 기본동작 테스트 (정상)
print(type(d2))
d2['a'] = 10.5
print(d2['a'])

try:
    d2['b'] = 'python'
except ValueError as e:     # 의도한 로직 작동
    print(e)

# - 그러나 .. 문제점
# - dict 의 get, set 같은 메서드 호출 시 "직접 재정의한 매직메서드를 사용하지 않음"

# - d2.get(..) 시 사용하는 매직메서드가 재정의한 메서드(__getitem__) 사용 X
print(d2.get('a'), '!=', d2['a'])

# - d2.update(..) 시 사용하는 매직메서드가 재정의한 메서드(__setitem__) 사용 X
# - 커스텀 로직 뚤고 ('b', 'python') 들어감
d2.update({'b': 'python'})
print(d2.get('b'))


print(d2.items())


print("-------------------------------")


# [ 'UserDict' 활용해서 Custom Dict 구현 (권장) ]
from collections import UserDict

class IntDictV3(UserDict):
    def __setitem__(self, key, value):
        if not isinstance(value, Real):
            raise ValueError("Value must be a real number.")
        super().__setitem__(key, value)

    def __getitem__(self, key):
        return int(super().__getitem__(key))


d3 = IntDictV3()

# - 기본동작 테스트 (정상)
d3['a'] = 10.5

# - .get() 메서드도 정의한 매직메서드 통해서 호출됨
print(d3['a'], '==', d3.get('a'))

# - 의도한 로직 정상 동작
try:
    d3['b'] = 'python'
except ValueError as e:
    print(e)

try:
    d3.update({'b': 'python'})
except ValueError as e:
    print(e)

# - get(..), set(..) 뿐만 아니라 생성자에서도 의도한 대로 동작
try:
    _ = IntDictV3(b='python')
except ValueError as e:
    print(e)

print(type(d3))
print(d3.data)
print(d3.items())

print("-------------------------------")


# [ 'UserDict' 상속한 다른 예시 ]
# - key 값 한정하기 + value 값 한정하기

class LimitedDict(UserDict):
    def __init__(self, key_set, min_value, max_value, *args, **kwargs):
        # 커스텀 로직에 필요한 인자 받기
        self._key_set = key_set
        self._min_value = min_value
        self._max_value = max_value

        # 그 외에는 부모 생성자로 전달하기
        # (ex. key=value 등)
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):

        # 커스텀 로직 구현
        if key not in self._key_set:
            raise KeyError("Invalid Key Name")
        if not isinstance(value, int):
            raise ValueError("Value Must Be an Integer Type")
        if value < self._min_value or value > self._max_value:
            raise ValueError("Value Max or Min Error")

        super().__setitem__(key, value)


limited_dict = LimitedDict(
    {'red', 'green', 'blue'}, 0, 255,
    red=10, green=20
)

# - 기본동작 테스트 (정상)
print(limited_dict.values())

limited_dict['blue'] = 99

try:
    limited_dict['xxx'] = 2
except KeyError as e:
    print(e)
