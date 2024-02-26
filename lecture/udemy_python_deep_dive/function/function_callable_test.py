def my_func():
    pass


class MyClass1:
    pass


class MyClass2:
    def __call__(self, *args, **kwargs):
        print('__call__ called')


# [ Callable ]
print(callable(my_func))            # Function -> True
print(callable(lambda : "HI"))      # Lambda -> True
print(callable(MyClass1))           # Class -> True
print(callable(10))                 # int -> False

instance1 = MyClass1()
instance2 = MyClass2()
print(callable(instance1))          # instance + Not __call__ -> False
print(callable(instance2))          # instance + __call__ -> True
