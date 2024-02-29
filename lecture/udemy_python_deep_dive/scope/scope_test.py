# [ Global Scope ]
# - 오직 Reference 만 할 경우 자동으로 Global 변수 참조

a = 'Global'


def my_func():
    print(a)       # 오직 Reference -> Global 변수 참조


my_func()


# [ Global Scope 2 ]
# - Function 내부에서 Assignment 있는 경우
def my_func2():
    a = 'Local'          # Assignemnt 있음 -> Local Scope 로 간주 및 참조
    print('Local a: ', a)


my_func2()
print('Global a : ', a)


# [ Global Scope 2_2 ]
# - 주의사항
# - Function 내부에서 Assignment 있는 경우 -> Local Scope
# - 따라서 Referecne 주의
def my_func2_2():
    # Assginment 구문이 있으면 -> Local 변수임
	print('Local2_2 a:', a) # 따라서 실행시점에 오류 (함수 정의자체는 됨)
	a = 'Local2'
	return

try:
    my_func2_2()
except:
    print('ERR')

# [ Function 내부에서 Global 변수 수정 ]
b = "From Global"


def my_func3():
    global b
    b = 'From Local'
    print('--Global 변수 수정--')
    return


print(f'Global 변수 수정 이전 -> {b}')
my_func3()
print(f'Global 변수 수정 이후 -> {b}')


# [ Function 내부에서 Global 변수 최초할당 ]
def my_func4():
    global c
    c = 'from my_func4'
    return


my_func4()
print('c: ', c)

