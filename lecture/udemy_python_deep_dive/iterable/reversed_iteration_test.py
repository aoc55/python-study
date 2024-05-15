# [ Example of Reversed Iteration ]
# - 직접 Reversed Iterator 생성함
# - 핵심은 reversed(..) 호출시 Iterator 가 반환되는 것이지, 원본 데이터가 변경되는건 아님

_SUITS = ('S', 'H', 'D', 'C')
_RANKS = tuple(range(2, 11)) + tuple('JQKA')  # (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')

from collections import namedtuple

Card = namedtuple('Card', 'rank, suit')


class CardDeck:
    def __init__(self):
        self.length = len(_SUITS) * len(_RANKS)

    def __len__(self):
        return self.length

    def __iter__(self):
        return self.CardDeckIterator(self.length)                   # 정방향 모드로 구현한 Iterator 생성 및 반환

    # reversed(..) 지원을 위해 구현 필요!
    def __reversed__(self):
        print("---- __reversed__ --- 호출")
        return self.CardDeckIterator(self.length, reverse=True)     # 역방향 모드로 구현한 Iterator 생성 및 반환

    # 정방향 & 역방향 모두 지원가능하게 Iterator 생성
    class CardDeckIterator:
        def __init__(self, length, reverse=False):
            self.length = length
            self.i = 0
            self.reverse = reverse

        def __iter__(self):
            return self

        def __next__(self):
            if self.i >= self.length:
                raise StopIteration
            else:
                if self.reverse:
                    index = self.length - 1 - self.i
                else:
                    index = self.i

                suit = _SUITS[self.i // len(_RANKS)]
                rank = _RANKS[self.i % len(_RANKS)]
                self.i += 1
                return Card(rank, suit)


# - 정방향 Iterator 활용
deck = CardDeck()
for card in deck:
    print(card)

# - 이때 Reverse 할려면?
# - 역방향 Iterator 활용
reversed_deck = reversed(CardDeck())  # ---- __reversed()__ --- 호출됨
for card in reversed_deck:
    print(card)


# [ Reversed Iteration By Python ]
# - Python 이 자동생성해주는 역방향 Iterator 활용
# - 전제조건으로 getItem 및 len 구현 필요
class Squares:
    def __init__(self, length):
        self.squares = [i ** 2 for i in range(length)]

    def __len__(self):
        return len(self.squares)

    def __getitem__(self, s):
        return self.squares[s]


# __len__, __getitem__ 구현함에 따라 "정 및 역방향 Iterator" 사용 가능
squares = Squares(5)

# - 정방향
for s in squares:
    print(s)

print("-----------")
# - 역방향
for s in reversed(squares):     # reversed() 결과로 index 기반으로 역방향으로 도는 iterator 반환됨
    print(s)
