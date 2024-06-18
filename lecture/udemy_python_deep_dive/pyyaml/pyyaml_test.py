import yaml     # pyyaml import

# [ PyYaml 실습 1 ]
# - 역직렬화
yaml_data = """
---
title: Parrot Sketch
actors:
    - first_name: John
      last_name: Cleese
      dob: 1939-10-27
    - first_name: Michale
      last_name: Palin
      dob: 1943-05-05
"""
# result = yaml.load(yaml_data, yaml.SafeLoader)
result = yaml.safe_load(yaml_data)
print(type(result), result)
print("----------------------------------------")


# [ PyYaml 실습 2 ]
# - 직렬화
d = {
    'a': 100,
    'b': False,
    'c': 10.5,
    'd': [1, 2, 3]
}

result = yaml.dump(d)
print(result)

# a: 100
# b: false
# c: 10.5
# d:
# - 1
# - 2
# - 3

print("----------------------------------------")

# [ PyYaml 실습 3 ]
# - Class Type 으로 직렬화 역직렬화
from datetime import date


# - Sample Class & Instance 생성
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'


p1 = Person("abcd", date(1994, 2, 4))
p2 = Person("zzzz", date(1988, 2, 10))
data = yaml.dump({'john': p1, "michale": p2})

print(data)
# john: !!python/object:__main__.Person
#   age: 1994-02-04
#   name: abcd
# michale: !!python/object:__main__.Person
#   age: 1988-02-10
#   name: zzzz

print("----------------------------------------")

# [ PyYaml 실습 4 ]
# - 역직렬화 시 주의사항
# - 안전하지 않은 Source 인 경우 'SafeLoader' or 'safeLoad' 사용

sample_yaml_data = """
john: !!python/object:__main__.Person
  name: abcd
  age: 1994-02-04
michale: !!python/object:__main__.Person
  name: zzz
  age: 1988-02-10
"""

data = yaml.load(sample_yaml_data, yaml.Loader)
print(data)
print(type(data['john']))                   # <class '__main__.Person'> -> 객체로 역직렬화 됨


print("----------------------------------------")


class PersonV2(yaml.YAMLObject):

    # Yaml 변환시 추가
    yaml_tag = '!PersonV2'
    # yaml_loader = yaml.SafeLoader

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'


p2_1 = PersonV2("abcd", date(1994, 2, 4))
p2_2 = PersonV2("zzzz", date(1988, 2, 10))

# - 직렬화
result = yaml.dump({'john': p2_1, "michale": p2_2})
print(result)

# - 다시 역직렬화
data = yaml.load(result, yaml.FullLoader)
# data = yaml.load(result, yaml.SafeLoader)
print(data)
