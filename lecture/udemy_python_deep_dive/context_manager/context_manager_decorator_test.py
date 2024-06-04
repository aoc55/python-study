# [ 기존의 방식 (복습) ]
# - (1) Generator 선언
# - (2) 이를 다루는 Context Manager 정의

# - (1) Generator 선언
def open_file(fname, mode='r'):
    print('>> Opening file...')
    f = open(fname, mode)
    try:
        yield f
    finally:
        print(">> Closing File ....")
        f.close()


# - (2) Context Manager 정의
class GenContextManager:
    def __init__(self, gen):
        self.gen = gen

    def __enter__(self):
        return next(self.gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('>>> Calling next() to perform cleanup in generator')
        try:
            next(self.gen)
        except StopIteration:
            pass
        return False

# - 활용
# - Generator 생성과 Ctx Manager 생성이 분리되어 있음
file_gen = open_file('test4.txt', 'w')
with GenContextManager(file_gen) as f:      # 따라서 Ctx Manager가 무슨 역할 하는지 알기 어려움
    f.writelines('hi')


# [ Decorator Ver - 직접구현 ]
# - 목표: Decorator 를 구현해서 '정의한 Generator'에 'Context Manager' 를 바로 적용하게 하자

# - (1) Context Manager 적용하는 Decorator 정의
def context_manager_dec(gen_fn):
    def helper(*args, **kwargs):
        # Encapsulation
        gen = gen_fn(*args, **kwargs)
        ctx = GenContextManager(gen)
        return ctx
    return helper

# - (2) 정의한 Generator 에서 Decorator 적용
@context_manager_dec
def open_file_v2(fname, mode='w'):
    print('>> Opening file...')
    f = open(fname, mode)
    try:
        yield f
    finally:
        print(">> Closing File ....")
        f.close()

# - (3) 활용
# - Openfile 실행 시 Decorator 통해서, 자동으로 Ctx Manager 생성 등 진행되어 사용 가능
with open_file_v2('test5.txt') as f:
    print(f.writelines('hi'))


# [ Decorator 라이브러리 사용 - 결론? ]
from contextlib import contextmanager


# - Generator 정의 후 관련 데코레이터 라이브러리 사용
@contextmanager
def open_file_v3(fname, mode='w'):
    print('>> Opening file...')
    f = open(fname, mode)
    try:
        yield f
    finally:
        print(">> Closing File ....")
        f.close()

# - 활용
with open_file_v2('test6.txt') as f:
    print(f.writelines('hi'))


# [ UseCase : Generator + Context Manager 사용예시 실습 1 ]
from time import perf_counter, sleep


@contextmanager
def timer():
    stats = dict()
    stats['start'] = perf_counter()
    try:
        yield stats
    finally:
        stats['end'] = perf_counter()
        stats['elapsed'] = stats['end'] - stats['start']


with timer() as stats:      # yield 반환 값을 as 'stats' 로 변수 할당
    sleep(2)


print(stats)        # With 절 자체 Scope 아님으로 현재도 'stats' 살아있음


# [ UseCase : Generator + Context Manager 사용예시 실습 2 ]
import sys


@contextmanager
def out_to_file(fname):
    current_stdout = sys.stdout            # 백업
    file = open(fname, 'w')
    sys.stdout = file                       # stdout 변경
    try:
        yield None                          # 변경 후 반환
    finally:
        file.close()
        sys.stdout = current_stdout        # stdout 복원


with out_to_file('test7.txt'):      # 해당 with 구간에서는 stdout 이 file 로 변경
    print("line 1")
    print("line 2")
    print("line 3")


# [ 참고 'redirect_stdout' 라이브러리 활용 ]
from contextlib import redirect_stdout

with open('test8.txt', 'w') as f:
    with redirect_stdout(f):
        print("test test test")