# [ Tuple Unpacking with Dummy Variables ]

sample = (2024, 3, 5, 9, 44, 'TUE', 'AM', 'SEOUL')

# Bad !!!
year = sample[0]
month = sample[1]
city = sample[-1]

print(f'year={year}, month={month}, city={city}')

# Bad !!!
year, month, city = sample[0], sample[1], sample[-1]
print(f'year={year}, month={month}, city={city}')

# * (Unpacking Operator) 사용하기
year, month, *_, city = sample
print(f'year={year}, month={month}, city={city}')
