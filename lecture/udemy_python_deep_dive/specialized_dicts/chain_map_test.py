# [ 기존 Unpack or Update 방식 ]

# - 대상 데이터
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'a': -1}  # 'a' Key 중복

# - Unpack 방식
d_by_unpack = {**d1, **d2, **d3}
print(d_by_unpack)      # 'a' Key 중복 -> 마지막 값인 '-1'로

# - update 방식
d_by_update = {}
d_by_update.update(d1)
d_by_update.update(d2)
d_by_update.update(d3)
print(d_by_update)      # # 'a' Key 중복 -> 마지막 값인 '-1'로

print("-------------------------------")

# [ 'ChainMap' 방식 ]
from  collections import ChainMap
d_chain = ChainMap(d1, d2, d3)

# - ChainMap != Dict
print(type(d_chain))                # <class 'collections.ChainMap'>
print(isinstance(d_chain, dict))    # False
print(d_chain)

# ChainMap (dict 와 달리) 순서보장 X
for x in d_chain:
    print(x, end=" -> ")            # e -> a -> c -> d -> b
print()

# - Edit ChainMap
d_chain['a'] = -999       # 수정
d_chain['new'] = -1       # 신규
print(d_chain)
# ChainMap({'a': -999, 'b': 2, 'new': -1}, {'c': 3, 'd': 4}, {'e': 5, 'a': -1})

print("  >> d1: ", d1)   # {'a': -999, 'b': 2, 'new': -1}
print("  >> d2: ", d2)
print("  >> d3: ", d3)


# - 세번째에 있음에도 예외
# - 첫번째 매핑만 바라봄
try:
    del d_chain['e']
except Exception as e:
    print(e)            # "Key not found in the first mapping: 'e'"


# - 원본 (Underlying) Dict 조작시 반영됨
d3['new_new'] = 777
print(d_chain['new_new'])       # 777

# - 부모 속성 추출
# - 가장 첫번째 매핑을 제외하고 리턴
# - 이를 통해 계층적으로 접근 가능

print(d_chain)
print(">", d_chain.parents)
print(">>", d_chain.parents.parents)
print(">>>", d_chain.parents.parents.parents)

print("-------------------------------")

# [ ChainMap 을 활용한 Use Case 예시 ]
config = {
    'host': 'aaa.bb.com',
    'port': 8080,
    'database': 'test',
    'user_id': 'abc',
    'user_pw': '1234'
}

local_config = ChainMap({}, config)

print(list(local_config.items()))

# chain map 에서만 변경
# 원본 객체는 안변경하고

local_config['user_id'] = 'local_test'
local_config['user_pw'] = 'local_1234'

print(list(local_config.items()))

print(local_config)
print(config)