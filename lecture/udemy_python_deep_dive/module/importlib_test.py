# [ importlib 이용한 모듈 로딩 ]
import importlib
import sys

# - 참고
my_module = 'math'
# import my_module -> 실패!

# - 로딩
my_math = importlib.import_module(my_module)

# - 로딩여부 확인
print('math' in sys.modules)    # True
print('my_math' in globals())   # True

# - 활용하기
print(my_math.sqrt(49))

