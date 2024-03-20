# [ Unpacking Tuple -> Bad Code ]
sample = (2024, 3, 5, 9, 44, 'TUE', 'AM', 'SEOUL')

# - Bad !!!
# - 매우 고정적인 코드로 중간에 Tuple 구조 변경 시 취약함
year = sample[0]
month = sample[1]
city = sample[-1]
print(f'year={year}, month={month}, city={city}')

# - Bad (2) !!!
year, month, city = sample[0], sample[1], sample[-1]
print(f'year={year}, month={month}, city={city}')


# [ Unpacking Tuple -> Good (with Unpakcing Operator) ]
# - Good
year, month, *_, city = sample # * (Unpacking Operator) + dummy Variable (__ 사용하기
print(f'year={year}, month={month}, city={city}')


# [ Tuple -> Immutable ]
a = (1, 2, 3)
a_id_1 = id(a)

a += (4, 5)
a_id_2 = id(a)

print(a_id_1 != a_id_2)  # True
