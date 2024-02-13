# [ N진법으로 변형 ]

def change_func(n, b):
    if b < 2 or n < 0:
        raise ValueError

    if n == 0:
        return 0

    # 변환
    digits = []
    while n > 0:
        # m = n % b
        # n = n // b
        (n, m) = divmod(n, b)
        digits.insert(0, m)

    # Encoding
    encoding_map = '0123456789ABCDEF'
    encoded_value = ''.join([encoding_map[x] for x in digits])  # Using List Comprehension
    # for d in digits:
    # encoded_value += encoding_map[d]

    return encoded_value


# Test
print(change_func(700, 16))
print(hex(700))


# [ 2, 8, 16 진법 ]
print(bin(10))      # 0b1010
print((oct(10)))    # 0o12
print(hex(10))      # 0xa

