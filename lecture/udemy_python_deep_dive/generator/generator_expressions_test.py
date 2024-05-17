# [ Generator Expressions ]

# - 기본
double_generator = (i * 2 for i in range(5))
print(list(double_generator))


# - Nested Generator Expression
start = 1
stop = 3
my_generator = ((i * j for j in range(start, stop + 1)) for i in range(start, stop + 1))  # Global 변수 접근가능
# - 출력
print([list(row) for row in my_generator])