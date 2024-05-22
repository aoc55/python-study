# [ tee 를 통한 iterable Copy 실습 ]

# - Sample Generator
def identity(n):
    for i in range(n):
        yield i


gen1 = identity(5)

# - tee 활용 Copy 수행
from itertools import tee
gen_copied_tuple = tee(gen1)        # 리턴 값은 tuple 임

print(gen1 is gen_copied_tuple[0])  # False -> 동일한 generator 가 아니라 Copied 된 Iterator 임
for x in gen_copied_tuple[0]:
    print(x)

print("--------------------------")

# [ tee 를 통한 iterable Copy 실습 2]
# - copy 시 갯수 지정 가능
gen_copied_tuple = tee(gen1, 3)

print("--------------------------")

# [ tee 를 통한 iterable Copy 실습 3]
# - 주의사항, iterator 가 아닌 iterable 을 파라미터로 전달시에도 결과는 iterator 임
my_list = [1, 2, 3, 4]              # Not Iterator !
list_copied_tuple = tee(my_list)    # Copy
print(list_copied_tuple[0] is list_copied_tuple[0].__iter__())  # True 결과값은 iterator!
print(type(list_copied_tuple[0]))
print(list(list_copied_tuple[0]))
