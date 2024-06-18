import serpy


# [ Serpy 실습 1 ]
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'


# Serializer 용도의 Class Define
class PersonSerializer(serpy.Serializer):
    name = serpy.StrField()
    age = serpy.IntField()


# Sample Data
person1 = Person('kgh', 20)

# 직렬화 수행
result = PersonSerializer(person1).data
print(result)

print("---------------------------------------")

# [ Serpy 실습 2 ]
# - 중첩된 직렬화 수행
class Movie:
    def __init__(self, title, year, actors):
        self.title = title
        self.year = year
        self.actors = actors


class MovieSerializer(serpy.Serializer):
    title = serpy.StrField()
    year = serpy.IntField()
    actors = PersonSerializer(many=True)        # 중첩된 직렬화


# - 샘플데이터
person1 = Person('kgh', 20)
person2 = Person('zzz', 10)

movie = Movie("title123", 1994, [person1, person2])

# - 직렬화 수행
result_data = MovieSerializer(movie).data
print(result_data)

print("---------------------------------------")
# - 직렬화 결과 -> json or yaml dump 수행
import json
import yaml

# - to Json
print(json.dumps(result_data))
# {"title": "title123", "year": 1994, "actors": [{"name": "kgh", "age": 20}, {"name": "zzz", "age": 10}]}

# - to Yaml
print(yaml.dump(result_data))
# actors:
# - age: 20
#   name: kgh
# - age: 10
#   name: zzz
# title: title123
# year: 1994

