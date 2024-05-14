import math


# [ Lazy Iterable 구현 전 1]
# - 문제점(1) :  radius setter 호출전까지 self.area는 없는 속성임
class Circle:
    def __init__(self, r):
        # ---> 객체 생성 후 바로 area  참조시 세팅이 안됨 오류
        # -->  __init__ 시 @radius.setter 호출되면서 -> c.area 세팅시키기
        # self._radius = r
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):  # __init__의 self.radius 통해서 호출됨
        self._radius = r
        self.area = math.pi * (r ** 2)


# 비효율적인 부분 존재
# - 매번 radius 설정할때마다 area 도 같이 계산이 되어짐
# - 만약 area가 관심이 없는 속성이였으면? 계산이 'wastefull' 함

c = Circle(1)
print(c.radius)
print(c.area)

c.radius = 2  # area 도 갱신됨
print(c.area)  # Update 됨

print("---------------------------")


# [ Lazy Iterable 1 ]
# - 개선 1차
# - 앞서 매번 raidus set 호출 시 area 계산되던 상황 개선
class Circle:
    def __init__(self, r):
        # self._radius = r
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        # 더이상 radius 업데이트 시 area 계산 및 갱신되지 않음

    # area 별도로 빼서 호출 시 마다 계산
    @property
    def area(self):
        print("Calculating Area....")
        return math.pi * (self.radius ** 2)


c = Circle(1)
print(c.area)
c.radius = 2
print(c.area)  # 단점 -> 호출하기만 해도 계속 Calculating Everty Time (radius 변화없으면 동일한 값임에도!!!)
print(c.area)  # Radius 변경 안해도 계속 계산... 비효율적
print(c.area)

print("---------------------------")


# [ Lazy Iterable 2 ]
# - 개선 2차, 하이브리드?
class Circle:
    def __init__(self, r):
        self.radius = r
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None  # radius 변경 시 area 도 새로 계산되어야 하므로 cache 값 삭제

    @property
    def area(self):
        if self._area is None:  # Caching 도입
            print("Calculating Area....")
            self._area = math.pi * (self.radius ** 2)
        return self._area


c = Circle(1)
print(c.area)  # Calculating Area....
print(c.area)
c.radius = 2  # area None 처리
print(c.area)  # Calculating Area.... (Radius 변경에 따라)
print(c.area)
print(c.area)

print("---------------------------")


# [ Lazy Iterable 3 ]
# - iterable, iterator 구현
class Factorials:
    def __init__(self, length):
        self.length = length

    def __iter__(self):
        return self.FactIter(self.length)

    class FactIter:
        def __init__(self, length):
            self.length = length
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.i >= self.length:
                raise StopIteration
            else:
                result = math.factorial(self.i)
                self.i += 1
                return result


# - 실제 Request 될때까지 -> 미리 팩토리얼 계산하지 않음 : Lazy Evaluation

facts = Factorials(5)
print(list(facts))

print("---------------------------")


# - Common 적인 방식
# - iterable 은 순전히 iterator 객체를 반환하는 방법에 대해서만 기술
class Factorials:
    def __iter__(self):
        return self.FactIter()

    class FactIter:
        def __init__(self):
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            result = math.factorial(self.i)
            self.i += 1
            return result


fact_iter = iter(Factorials())
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))
