# [ Chaining ]
# - 실제 매우 자주 쓰임


gen1 = (i for i in range(4))
gen2 = (i for i in range(4, 8))
gen3 = (i for i in range(8, 12))


for gen in gen1, gen2, gen3:
    print("")
    for item in gen:
        print(item, end=", ")
        # 0, 1, 2, 3,
        # 4, 5, 6, 7,
        # 8, 9, 10, 11,

print("")
print("------------------------")


gen1 = (i for i in range(4))
gen2 = (i for i in range(4, 8))
gen3 = (i for i in range(8, 12))


def chain_iterables(*iterables):
    for iterable in iterables:
        yield from iterable


custom_chain = chain_iterables(gen1, gen2, gen3)
print(list(custom_chain))       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


print("------------------------")

from itertools import chain


gen1 = (i for i in range(4))
gen2 = (i for i in range(4, 8))
gen3 = (i for i in range(8, 12))
tools_chain = chain(gen1, gen2, gen3)
print(list(tools_chain))      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


print("------------------------")


def identity():                          # 호출 시 아래 Generator 가 순차 반환
    print('yield1')
    yield (i for i in range(4))          # Generator 1
    print('yield2')
    yield (i for i in range(4, 8))       # Generator 2
    print('yield3')
    yield (i for i in range(8, 12))      # Generator 3


for gen in identity():
    print(gen)
    #     <generator object identity.<locals>.<genexpr> at 0x1030c6a50>
    #     <generator object identity.<locals>.<genexpr> at 0x1030c6eb0>
    #     <generator object identity.<locals>.<genexpr> at 0x1030c6a50>

print("------------------------")

for i in chain(*identity()):    # Unpacking Eagerly! -> genenarter 반환되는 yield 를 한꺼번에 수행
    print(i)
    # yield1
    # yield2
    # yield3
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9
    # 10
    # 11

print("------------------------")

chain_iterables = chain.from_iterable(identity())
for i in chain_iterables:
    print(i)
    # yield1
    # 0
    # 1
    # 2
    # 3
    # yield2
    # 4
    # 5
    # 6
    # 7
    # yield3
    # 8
    # 9
    # 10
    # 11
