# [ Single Inheritance 실습 ]
class Person:

    def eat(self):
        print("eat.....")


class Teacher(Person):
    pass


class Student(Person):
    pass

# - type(..), isinstance(obj, class)
p1 = Person()
print(isinstance(p1, Person))       # True
print(isinstance(p1, Teacher))      # False
print(type(p1))                     # <class '__main__.Person'>

t1 = Teacher()
print(isinstance(t1, Teacher))      # True
print(isinstance(t1, Person))       # True
print(type(t1))                     # <class '__main__.Teacher'>


# - issubclass (..)
print(issubclass(Teacher, Person))  # True
print(isinstance(Student, Teacher)) # False

try:
    print(issubclass(p1, Student))      # instance 가 아닌 클래스
except Exception as e:
    print(e)

