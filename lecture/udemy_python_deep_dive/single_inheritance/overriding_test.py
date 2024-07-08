 # [ Overriding 실습1 ]
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name})'


class Student(Person):
    pass


p1 = Person('abc')
print(p1.__repr__())

s1 = Student('kgh')
print(s1.__repr__())


# [ Overriding 실습2 ]
class Parent:

    def method1(self):
        print("parent -> method1")

    def method2(self):
        print("parent -> method2")

    def method3(self):
        print("parent -> method3")

    def run(self):
        self.method1()
        self.method2()
        self.method3()


class Child(Parent):
    # method 2 만 오버라이딩
    def method2(self):
        print("child -> method2")

p1 = Parent()
p1.run()

c1 = Child()
c1.run()