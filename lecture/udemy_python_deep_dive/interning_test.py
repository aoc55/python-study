# [ Int Interning ]
# int 의 경우 -5~256 까지 Singleton 으로 최적화 되어 있음
a = 10
b = 10
print(a is b)       # True

# [ String Interning ]
# string 의 경우 _, 소문자, 숫자로만 구성 될 경우
a = 'hello_str'
b = 'hello_str'
print(a is b)               # True

