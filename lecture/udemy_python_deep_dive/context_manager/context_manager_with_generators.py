# [ Generator '직접' 사용 패턴 ]
# - Generator 정의
def my_gen():
    try:
        print("Create Context and Yielding object")
        yield [1, 2, 3, 4]
    finally:
        print("Exit Context And Cleaning Up")


# - 마치 Context Manager 사용 패턴처럼 사용
gen = my_gen()
lst = next(gen)
print(lst)
try:
    next(gen)
except StopIteration:
    pass            # StopIteration 발생 시 PASS 처리

print("------------------------------")


# [ Context Manager For Generator 정의 1 ]
# - Context Manager 정의 -> __enter__, __exit__ 구현
class GenCtxManager:
    def __init__(self, gen_func):
        self._gen = gen_func

    def __enter__(self):
        return next(self._gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False


# - Test
test_gen = my_gen()
with GenCtxManager(test_gen) as obj:
    print(obj)


print("------------------------------")


# [ Context Manager For Generator 정의 2 ]
class GenCtxManagerV2:
    def __init__(self, gen_func, *args, **kwargs):
        self._gen = gen_func(*args, **kwargs)        # 여기서 Generator 생성

    def __enter__(self):
        return next(self._gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False


# - Sample 용 Generator
def open_file(fname, mode):
    f = open(fname, mode)
    try:
        yield f
    finally:
        f.close()


# - Test
with GenCtxManagerV2(open_file, "test3.txt", 'r') as f:
    print(f.readlines())
