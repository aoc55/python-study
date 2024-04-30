

from time import perf_counter
from collections import namedtuple
import argparse
import zipfile

print('Loading Timing.py .... ')

Timing = namedtuple('Timing', 'repeats elapsed average')


def time_it(code, repeat=10):
    code = compile(code, filename='<string>', mode='exec')
    start = perf_counter()

    for _ in range(repeat):
        exec(code)



    end = perf_counter()
    elapsed = end - start
    average = elapsed / repeat
    return Timing(repeat, elapsed, average)


# 직접 실행할 때를 위해
if __name__ == '__main__':

    # Argument Parser 정의
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('code',
                        type=str,
                        help='The python code snippet to time.')

    parser.add_argument('-r', '--repeats',
                        type=int,
                        default=10,
                        help='Number of times to repeat the test')

    args = parser.parse_args()

    print(args.code)
    print(args.repeats)
    print(type(args.code))

    # 시작
    result = time_it(code=str(args.code), repeat=args.repeats)
    print(result)