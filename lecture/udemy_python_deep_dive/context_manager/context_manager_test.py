# [ Context Manager 직접 try ~ finally 구문]
def my_func():
    try:
        10 / 0
    except ZeroDivisionError:
        return
    finally:                    # 매번 finally 구문 작성하는게 귀찮음 !
        print("finally run !")

def my_func2():
    try:
        f = open("test.txt", 'w')
        # do Something !
    finally:                    # 매번 finally 구문 작성하는게 귀찮음 !
        f.close()


# [ Context Manager 인 'Open' 활용 ]
with open('test.txt', 'w') as file:
    # file ... do Something
    print("inside with: file closed?", file.closed)

# - 이때  알아서 closed 처리 등 진행해줌
print('after with: file closed?', file.closed)


# [ with 절의 Scope 관련]
# - with 절은 별도의 Scope 없음
with open('test2.txt', 'r') as f:
    row = next(f)               # row 역시 with 절과 동일 Scope 내 (여기서는 Global)


# - with 절 이후 'f'와 'row' 그대로 접근가능! (동일 Scope 에 있었으므로)
print(f.closed)
print(row)


# [ 직접 정의한 클래스에 Context Protocol 구현해보기 ]
class MyContext:
    def __init__(self):
        print("__init__ called .... !")
        self.obj = None

    # enter 구현
    def __enter__(self):
        print("entering context ... !")
        self.obj = 'the Return Object'
        return self.obj

    # exit 구현
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


# [ 직접 정의한 클래스에 Context Protocol 구현해보기 2 ]
# - Resource 라는 타겟 클래스 정의
# - ResourceManager 가 Resource 를 관리하는 Context Manager 역할 수행하기
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


# [ 직접 정의한 클래스에 Context Protocol 구현해보기 3 ]
# - 직접 File 클래스(래핑?)를 정의해서 프로토콜 구현해보기
class File:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        print('opening file ... !')
        self.file = open(self.name, self.mode)
        return self.file            # File 을 반환

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('closing file ... !')
        self.file.close()                       # File 닫기
        return False


with File('test.txt', 'w') as f:
    f.write('This is a late parrot!')

with File('test.txt', 'r') as f:
    print(f.readlines())


# [ 직접 정의한 클래스에 Context Protocol 구현해보기 4]
# - 직접 File 클래스(래핑?)를 정의해서 프로토콜 구현해보기
# - 위와 달리 enter 의 반환으로 Context Manager인 self 직접 반환
# - 그러면 반환 받아서 사용하는 방식도 달라져야함
class FileV2:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        print('opening file ... !')
        self.file = open(self.name, self.mode)
        return self     # File 아 아닌 Context Manager 자체 반환
        # 참고로 무엇이든 반환할 수 있음

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('closing file ... !')
        self.file.close()
        return False


with FileV2('test.txt', 'w') as fm:
    fm.file.write('This is a late parrot! 222')     # 대신 사용하는 곳에서 변경 필요

with FileV2('test.txt', 'r') as fm:
    print(fm.file.readlines())
