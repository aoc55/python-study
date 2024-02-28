from functools import reduce
import operator

# [ Operator 1 ]
print(reduce(operator.add, [1, 2, 3, 4, 5]))
print(operator.or_(True, False))
print(operator.mul(10, 20))


# [ Operator 2 ]
print(operator.concat('hi~ ', 'everyone'))
print(operator.getitem([1, 2, 3, 4, 5], 0))


# [ Operator - itemGetter ]
f = operator.itemgetter(0)
print(f([1, 2, 3, 4, 5]))
print(f('everyone'))

f2 = operator.itemgetter(0, 1, 2)
print(f2('everyone'))                   # ('e', 'v', 'e')


# [ Operator - attrGetter ]

class MyClass:
    a = 10
    b = 20

    def test1(self):
        print("test1~")

instance1 = MyClass()

# - attr 추출
f_attr_1 = operator.attrgetter('a')
print(f_attr_1(instance1))

# - attr 추출 (복수)
f_attr_2 = operator.attrgetter('a', 'b')
print(f_attr_2(instance1))

# - attr 추출 -> callable -> 호출
f_attr_3 = operator.attrgetter('test1')
f_attr_3(instance1)()


# [ Operator - attrGetter 2 ]
s = 'python'
f = operator.attrgetter('upper')
print(f(s)())   # s.upper()


# [ Oeprator - methodCaller 1]
print(operator.methodcaller('upper')('python'))

# [ Oeprator - methodCaller 2]
operator.methodcaller('test1')(instance1)



