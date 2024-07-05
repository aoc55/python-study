# [ Class Body Scope ]

def ext_full_version():
    return f'{Language.MAJOR}.{Language.MINOR}.{Language.REVISION}'
    # return f'{MAJOR}.{MINOR}.{REVISION}'
    # 불가 Method Scope 는 별도임므로


class Language:

    # Class Attributes
    MAJOR = 3
    MINOR = 7
    REVISION = 4

    def __init__(self, major, minor, revision):
        self.MAJOR = major
        self.MINOR = minor
        self.REVISION = revision

    @property
    def version(self):
        return f'{self.MAJOR}.{self.MINOR}.{self.REVISION}'

    @classmethod
    def cls_version(cls):
        return f'{cls.MAJOR}.{cls.MINOR}.{cls.REVISION}'

    @staticmethod
    def static_version():
        return f'{Language.MAJOR}.{Language.MINOR}.{Language.REVISION}'

    ext_version = ext_full_version


l = Language(5, 5, 5)
print(l.version)                # Instnace Attribute
print(l.cls_version())          # Class Attrbitue
print(l.static_version())       # Class Attribute


print(Language.ext_version())


print("---------------------")


# [ Unexpected -> 버그 발생 예시 1 ]
def gen_class():

    MAJOR = -1
    MINOR = -1
    REVISION = -1

    class InLanguage:

        # 의도한 값
        MAJOR = 3
        MINOR = 7
        REVISION = 4

        @classmethod
        def version(cls):
            # return f'{cls.MAJOR}.{cls.MINOR}.{cls.REVISION}'
            # Class Attribute 가 아닌 다른데서
            return f'{MAJOR}.{MINOR}.{REVISION}'

    return InLanguage


test = gen_class()
print(test.version())


import inspect
print(inspect.getclosurevars(test.version))



# [ Unexpected -> 버그 발생 예시 2 ]

name = 'kgh'            # Module's Namescope


class MyClass:
    name = 'Ryamond'
    list_1 = [name] * 3

    # [주의]
    # - list comprehension -> 간결한 'function 일뿐'
    # - function -> 별도 scope -> class 내가 아닌 global 내 name 가져옴
    list_2 = [name for i in range(3)]

    @classmethod
    def hello(cls):
        # return '{} says hello'.format(cls.name)
        # 모듈에서 가져와버림
        return '{} says hello'.format(name)


print(MyClass.hello())
print(MyClass.list_1)
print(MyClass.list_2)
