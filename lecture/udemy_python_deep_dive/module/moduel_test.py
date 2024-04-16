# [ Namespace 조회 ]
global_var = -1
print('globals = ', globals())
print('locals = ', locals())
print(globals() == locals())        # True


def dummy_func():
    func_var = 1
    print("func's locals = ", locals())


dummy_func()    # func's locals =  {'func_var': 1}


# [ Module 로딩 ]
import math
print(globals()['math'])
# <module 'math' from '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib
# /python3.9/lib-dynload/math.cpython-39-darwin.so'>

print(type(math))   # <class 'module'>

print(math.sqrt(49))
print(globals()['math'].sqrt(49))


# [ Module 재 로딩 ? ]
print(id(math))                 # 4369816848


def dummy_func2():
    import math                 # 함수 내부에서 다시 Import
    print('id(math) in dummy_func2  = ', id(math))


dummy_func2()                   # 4369816848
# - Id 동일함을 알 수 있음
# - 즉, 본질적으로 Singletone Object


# [ Module 목록 조회 ]
import sys
print(sys.modules)
print(sys.modules['math'])
print(id(sys.modules['math']))  # 4369816848


# [ Module Introspection ]
print(math.__name__)
print(math.__dict__)
print(math.__dict__['sqrt'](49)) # 7.0


# [ Module 은 ModuleType의 인스턴스 ]
import types
import fractions

print(isinstance(math, types.ModuleType))       # True
print(isinstance(fractions, types.ModuleType))  # True