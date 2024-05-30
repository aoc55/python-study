# [ Context Manager 직접 구현 실습 ]
# - Iterable Protocol 과 Contenxt Protocol 구현함
# - 직접 정의한 클래스에서 Protocol 구현을 통해 활용 예시

class DataIterator:
    def __init__(self, fname):
        self._fname = fname         # File 이름
        self._f = None              # File 객체

    # Iterator Protocol 구현

    def __iter__(self):
        return self

    def __next__(self):
        row = next(self._f).strip('\n')
        return row

    # Context Protocol 구현

    def __enter__(self):
        self._f = open(self._fname, 'r')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self._f.closed:
            self._f.close()
        return False


# with 절을 통한 사용
my_iterator = DataIterator('test3.txt')
with my_iterator as m:
    for row in m:
        print(row)