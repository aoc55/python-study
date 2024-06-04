# [ Nested Context Manager - 1 ]
# - 동시에 여러 Context 를 다뤄야 할 경우 How ?
# - 대상 Context 대상이 이미 정해진 경우 -> 아래처럼
with open('file1.txt', mode='r') as f1:
    with open('file2.txt', mode='r') as f2:
        with open('file3.txt', mode='r') as f3:
            print(f1.readlines())
            print(f2.readlines())
            print(f3.readlines())

print("---------------------")

# [ Nestd Context Manager - 2 ]
# - 대상 Context 대상이 정해지지 않은 경우
# - EX) 어떤 디렉토리 내에 있는 모든 파일 (N) 등
from contextlib import contextmanager


# - 직접 정의한 context Manager
@contextmanager
def open_file(f_name):
    print(f'opening {f_name}')
    f = open(f_name)
    try:
        yield f
    finally:
        print(f'closing {f_name}')
        f.close()


# - 가변적인 갯수의 Context Manager 를 다룰 수 있는 클래스 직접 정의
class NestedContexts:
    def __init__(self, *contexts):          # Context manager 들 입력 및 리스트 보관
        self._enters = []
        self._exits = []
        self._values = []

        for ctx in contexts:
            self._enters.append(ctx.__enter__)
            self._exits.append(ctx.__exit__)

    def __enter__(self):
        for enter in self._enters:
            self._values.append(enter())        # 각 __enter__ 실행
        return self._values                     # 각 __enter__ 실행 결과값 반환

    def __exit__(self, exc_type, exc_val, exc_tb):
        for ex in self._exits[::-1]:            # 각 __exit__ 실행 (역순으로)
            ex(exc_type, exc_val, exc_tb)
        return False


# - 활용
f_names = 'file1.txt', 'file2.txt', 'file3.txt'
contexts = [open_file(f_name) for f_name in f_names]        # 개별적으로 Context manager 생성
with NestedContexts(*contexts) as files:
    print("do work here")


print("---------------------")


# [ Nestd Context Manager - 3 ]
# - 위에서 with 절 밖에서 개별적으로 Context Manager 생성 후 전달필요
# - 이를 개선하자
class NestedContextsV2:
    def __init__(self):
        self._exits = []

    def __enter__(self):
        return self

    def enter_context(self, ctx):               # Context 등록 받는 별도의 메서드 선언
        self._exits.append(ctx.__exit__)
        value = ctx.__enter__()
        return value

    def __exit__(self, exc_type, exc_val, exc_tb):
        for ex in self._exits[::-1]:      # 역순으로 실행
            ex(exc_type, exc_val, exc_tb)
        return False


f_names = 'file1.txt', 'file2.txt', 'file3.txt'
with NestedContextsV2() as stack:
    files = [stack.enter_context(open_file(f)) for f in f_names]        # with 절 안에서 각 context manager 등록
    print("do work")

print("---------------------")


# [ Nestd Context Manager - 4 ]
# - 결론적으로 라이브러리 사용
from contextlib import ExitStack

f_names = 'file1.txt', 'file2.txt', 'file3.txt'
with ExitStack() as stack:
    files2 = [stack.enter_context(open_file(f)) for f in f_names]        # with 절 안에서 각 context manager 등록
    print("do work")

