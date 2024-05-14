# [ Soriting Iterables ]
# - sorted() 함수의 argument 는Seqeunce Type 이 아닌 Iterable 이면 지원
# - Iterable 객체 구현 후 sorted() Test
import random


class RandomInts:
    def __init__(self, length, *, seed=0, lower=0, upper=10):
        self.length = length
        self.seed = seed
        self.lower = lower
        self.upper = upper

    def __len__(self):
        return self.length

    def __iter__(self):
        return self.RandomIterator(self.length, seed=self.seed, lower=self.lower, upper=self.upper)

    # Iterator 객체
    class RandomIterator:
        def __init__(self, length, *, seed=0, lower=0, upper=10):
            self.length = length
            self.seed = seed
            self.lower = lower
            self.upper = upper
            self.num_request = 0
            random.seed(seed)

        def __iter__(self):
            return self

        def __next__(self):
            if self.num_request >= self.length:
                raise StopIteration
            else:
                result = random.randint(self.lower, self.upper)     # Lazy ?
                self.num_request += 1
                return result


# 활용
random_ints = RandomInts(10, seed=0, lower=0, upper=20)

# 출력
for v in random_ints:
    print(v)

# sorted 사용
print("Before Sorted -> ", list(random_ints))
print("After Sorted -> ", sorted(random_ints))


