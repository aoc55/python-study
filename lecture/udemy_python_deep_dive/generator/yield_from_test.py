# [ yield from 실습 ]
# - 기본
def brands(*files):                         # Generator
    for f_name in files:
        with open(f_name) as f:
            for line in f:                  # f -> iterator
                yield line.strip('\n')      # 'generator'의 yield 구문은 iterator 에서 수행 (delegate)

# - v2
# - for .. yield.. -> yield from 'other iterator' 로 대체
def brands_v2(*files):                      # Generator
    for f_name in files:
        with open(f_name) as f:
            yield from f                    # yield from '다른 Iterator'
# - 이때 yield from 사용하면서 line.strip('\n') 등 사용불가


# - v3
# - 관심사 다름에 따른 메서드 분리 수행

def get_clean_data(file):
    with open(file) as f:
        for row in f:
            yield row.strip('\n')

def brands_v3(*files):
    for f_name in files:
        clean_data = get_clean_data(f_name)
        for line in clean_data:
            yield line


# - v4
# - v3 기반에 다시 yield from 사용하기!
def brands_v4(*files):
    for f_name in files:
        yield from get_clean_data(f_name)

