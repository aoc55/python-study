# [ Descriptor Test 1 ]
from datetime import datetime


# - 'Non-Data' Descriptor 정의
class TimeUTC:

    def __get__(self, instance, owner):
        print(">>> __get__ 호출")
        return datetime.utcnow().isoformat()


# - Descriptor 를 '활용'하는 클래스
class Logger:

    # class Attribute 에 Descriptor 지정
    current_time = TimeUTC()


# - 인스턴스 생성 및 get 호출
logger = Logger()
print(logger.current_time)       # 접근 -> Descriptor __get__ 호출됨
print("")

# - IF instnace 에서 set Attribute 호출
# - 'Non-Data" Descriptor 임으로 set 미정의
# - 따라서 기존 Descriptor Attribute 는 가려짐
logger.current_time = 'new'
print('current_time' in logger.__dict__)       # True -> instance __dict__ 내
print(logger.current_time)

print("-------------------------------------")


# [ Descriptor Test 2-1 ]
# - @property 활용
from random import choice, seed


class Deck:

    @property
    def suit(self):
        return choice(('S', 'D', 'H', 'C'))

    @property
    def card(self):
        return choice(tuple('23456789JQKA') + ('10', ))


d = Deck()
seed(0)
for _ in range(5):
    print(d.card, d.suit)
print()


# [ Descriptor Test 2-2 ]
# - 'Non-Data' Descriptor 직접 정의
class Choice:

    def __init__(self, *choices):
        self.choices = choices

    def __get__(self, instance, owner):
        print(">>>> choice's __get__ call")
        return choice(self.choices)


# - Descritor 활용 버전 클래스 정의
class DeckV2:

    # class attribute -> Descriptor 사용
    suit = Choice('S', 'D', 'H', 'C')
    card = Choice(*'23456789JQKA', '10')


d2 = DeckV2()
seed(0)
for _ in range(5):
    print(d2.card, d2.suit)
print()


# - 정의한 Descriotr 활용하는 또 다른 예제
class Dice:

    # class attribute -> Descriptor 사용
    die_1 = Choice(1, 2, 3, 4, 5, 6)
    die_2 = Choice(1, 2, 3, 4, 5, 6)


dice = Dice()
print(dice.die_1)
print(dice.die_2)
