# [ Grouping ]
test_data = [
    (1, 10, 100),
    (1, 11, 101),
    (1, 12, 102),
    (2, 20, 200),
    (2, 21, 201),
    (3, 30, 300),
    (3, 31, 301),
    (3, 32, 302)
]


# - Check Lazy Iterator
def is_iterator(target):
    return iter(target) is target and '__next__' in dir(target)

# - Groupboy 실습
from itertools import groupby

grouping_result = groupby(test_data, lambda x: x[0])
print("Iterator ? ", is_iterator(grouping_result))


for key, sub_iterator in grouping_result:
    print('Key = ', key, "Iterator = ", is_iterator(sub_iterator))      # (Key, Iterator) 반환
    for v in sub_iterator:
        print("  -> ", v)

    # Key = 1
    # Iterator = True
    # ->  (1, 10, 100)
    # ->  (1, 11, 101)
    # ->  (1, 12, 102)
    # Key = 2
    # Iterator = True
    # ->  (2, 20, 200)
    # ->  (2, 21, 201)
    # Key = 3
    # Iterator = True
    # ->  (3, 30, 300)
    # ->  (3, 31, 301)
    # ->  (3, 32, 302)


