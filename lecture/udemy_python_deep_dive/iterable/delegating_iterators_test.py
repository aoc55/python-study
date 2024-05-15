# [ Delegating Iterator ]
# - Iterator 를 직접 구현할 필요 없이, 이미 지원하는 type 이라면 해당 Iterator 활용 (위임)
# - 심플한 컨셉이지만 자주 사용됨 !!
from collections import namedtuple
Person = namedtuple('Person', 'first last')


# - 직접 정의한 Iterable Class
class PersonNames:
    def __init__(self, persons):
        try:
            self._persons = [person.first.capitalize() + ' ' + person.last.capitalize() for person in persons]
        except (TypeError, AttributeError):
            self._persons = []

    # delegating iterator !!
    # list 에 의해서 생성된 iterator 활용
    def __iter__(self):
        return iter(self._persons)


# - 활용
persons = [Person('f1', 'l1'), Person('f2', 'l2'), Person('f3', 'l3')]
person_names = PersonNames(persons)

# - iterator 추출 및 활용
iterator = iter(person_names)
for v in iterator:
    print(v)

