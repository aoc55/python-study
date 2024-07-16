# [ Enumeration Basic ]
import enum


class Color(enum.Enum):
    red = 1
    green = 2
    blue = 3


class Status(enum.Enum):
    PENDING = 'pending'
    RUNNING = 'running'
    COMPLETED = 'completed'


class UnitVector(enum.Enum):
    V1D = (1, )
    V2D = (1, 1)
    V3D = (1, 1, 1)


# - Instance
print("----Instance----")
print(Status.RUNNING)
print(isinstance(Status.RUNNING, Status))
print(Status.RUNNING.name, Status.RUNNING.value)

# - Equality
print("----Equality----")
print(Status.RUNNING is Status.RUNNING)         # True
print(Status.RUNNING == Status.RUNNING)         # True
print(Status.PENDING is Status.COMPLETED)       # False
print(Status.PENDING == Status.COMPLETED)       # False


# immutable
print("----immutable----")

try:
    Status.PENDING.value = 'NEW-VALUE'
except AttributeError as e:
    print(e)
    # can't set attribute

try:
    Status['NEW-KEY'] = 'NEW-VALUE'
except TypeError as e:
    print(e)
    # 'EnumMeta' object does not support item assignment


# - get By Value
print("----getByValue----")
print(Status('pending'), Status('running'))
print(getattr(Status, 'PENDING'), getattr(Status, 'RUNNING'))

try:
    print(Status('NOT_EXIST_VALUE'))
except ValueError as e:
    print(e)                # 'NOT_EXIST_VALUE' is not a valid Status

# - get By Name
print("----getByName----")
print(Status['PENDING'], Status['RUNNING'])
print(UnitVector['V1D'], UnitVector['V2D'])

try:
    print(Status['NOT_EXIST_KEY'])
except KeyError as e:
    print(e)                # KeyError: 'NOT_EXIST_KEY'


# - Membership Test
print("----Membership----")
print(Status.RUNNING in Status)
try:
    print('pending' in Status)
except TypeError as e:
    print(e)


def is_enum_member(en, name):
    return getattr(en, name, None) is not None


print(is_enum_member(Status, 'PENDING'))        # True
print(is_enum_member(Status, 'NOT_EXIST'))      # False

print(Status.__members__['PENDING'] is Status.PENDING)  # True


# - iteration
print("----iteration----")
print(hasattr(Status, '__iter__'))      # True
print(list(Status))
print(list(Color))


# - hashable
print("----hashable----")


class Person:
    def __hash__(self):
        return None


try:
    print(hash(Person()))
except TypeError as e:
    print(e)            # TypeError: __hash__ method should return an integer


class Family(enum.Enum):
    person1 = Person()
    person2 = Person()


print(hash(Family.person1))         # Enumeration -> Hashable
my_dict = {
    Family.person1: 'abc',          # Key 로 사용 -> Hashable
    Family.person2: 'zzz'
}
print(my_dict)


# Can't Extend
print("----CAN'T EXTEND----")

class EnumBase(enum.Enum):
    ONE = 1

try:
    class EnumExt(EnumBase):
        TWO = 2
except TypeError as e:
    print(e)
    # EnumExt: cannot extend enumeration 'EnumBase'

