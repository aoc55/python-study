import inspect

# [ Function vs Method ]
# my_func1의 comment ~
def my_func1():
    print("my_func1()")


class MyClass1:
    def method1(self):
        print("method1")


instance1 = MyClass1()

print(inspect.isfunction(my_func1))                 # True
print(inspect.ismethod(my_func1))                   # False
print(inspect.isroutine(my_func1))                  # True

print(inspect.isfunction(instance1.method1))        # False
print(inspect.ismethod(instance1.method1))          # True
print(inspect.isroutine(instance1.method1))         # True

# [ Code 얻기 ]
print(inspect.getsource(my_func1))                  # String 으로 Code 출력

# [ 소속된 모듈 얻기 ]
print(inspect.getmodule(instance1.method1))         # <module '__main__' from ...
print(inspect.getmodule(print))                     # <module 'builtins' (built-in)> ..

# [ Comment (주석 획득) ]
print(inspect.getcomments(my_func1))                # def 위의 주석 획득 (docString 과 다름)


# [ Signature 획득 ]
def my_func2(a: 'a string',
             b: int = 1,
             *args: 'additional positional args',
             kw1: 'first kw',
             kw2: 'second kw'= 10,
             **kwargs: 'additional keyworad args') -> str :
    """
    this is docString
    for my_func2
    """
    pass


for param in inspect.signature(my_func2).parameters.values():
    print("")
    print('Name:', param.name)
    print('Default:', param.default)
    print('Antt:', param.annotation)
    print('Kind:', param.kind)
    # Name: kw2
    # Default: 10
    # Antt: second
    # kw
    # Kind: KEYWORD_ONLY
