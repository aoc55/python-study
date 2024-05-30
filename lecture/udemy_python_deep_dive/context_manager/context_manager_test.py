def my_func():
    try:
        10 / 0
    except ZeroDivisionError:
        return
    finally:
        print("finally run !")

def my_func2():
    try:
        f = open("test.txt", 'w')
        # do Something !
    finally:
        f.close()


# [ Context Protocol 구현한 Open ]
with open('test.txt', 'w') as file:
    # file ... do Something
    print("inside with: file closed?", file.closed)
    pass

print('after with: file closed?', file.closed)

# [ with -> Scope 없음!]
with open('test2.txt', 'r') as f:
    row = next(f)


# - with 절 이후 row 그대로 살아있음
print(f.closed)
print(row)

# [ Context Protocol 직접 구현 ]
class MyContext:
    def __init__(self):
        print("__init__ called .... !")
        self.obj = None

    def __enter__(self):
        print("entering context ... !")
        self.obj = 'the Return Object'
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exiting context ... !")
        if exc_type:
            print(f'---> Error Occured: {exc_type}, {exc_val}')

        # return False # 예외 발생 시 not Slience
        return True # 예외 발생 시 Slicence

ctx = MyContext()
print('created custom context !!')
with ctx as obj:
    print(f"-> Inside with Block | obj={obj}")
    raise ValueError("의도된 예외")

# - cotext local scope 있는거 아님!!
print("with 절 밖에서 접근 =", obj)



class Resource:
    def __init__(self, name):
        self.name = name
        self.state = None

class ResourceManager:
    def __init__(self, name):
        self.name = name
        self.resource = None

    def __enter__(self):
        print("entering Context")
        self.resource = Resource(self.name)
        self.resource.state = 'created'
        return self.resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exiting context")
        self.resource.state = 'destroyed'
        if exc_type:
            print('error occured')
        return False


resource_manager = ResourceManager('spam')
with resource_manager as res:
    print(f'(In With) --- > {res.name} = {res.state}')

# 외부에서 접근
print(f'(Out With) --- > {res.name} = {res.state}')


# 직접 File 실습
class File:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        print('opening file ... !')
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('closing file ... !')
        self.file.close()
        return False


with File('test.txt', 'w') as f:
    f.write('This is a late parrot!')

with File('test.txt', 'r') as f:
    print(f.readlines())



# 직접 File 실습
class FileV2:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        print('opening file ... !')
        self.file = open(self.name, self.mode)
        return self     # File 아 아닌 Context Manager 자체 반환
        # 무엇이든 반환할 수 있음

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('closing file ... !')
        self.file.close()
        return False


with FileV2('test.txt', 'w') as fm:
    fm.file.write('This is a late parrot! 222')

with FileV2('test.txt', 'r') as fm:
    print(fm.file.readlines())
