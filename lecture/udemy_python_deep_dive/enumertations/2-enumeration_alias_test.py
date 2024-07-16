# [ Enumeration Alias ]
import enum


class NumSides(enum.Enum):
    Triangle = 3

    # Same Value
    Rectangle = 4       # -> Master (?)
    Square = 4          # -> Alias


# -'is', 'in'
print("----is, in----")
print(NumSides.Rectangle is NumSides.Square)    # True
print(NumSides.Square is NumSides.Rectangle)    # True

print(NumSides.Square in NumSides)              # True
print(NumSides.Rectangle in NumSides)           # True


# - get By Name, Value
print("----getByName/Value----")
print(NumSides(4))                              # NumSides.Rectangle
print(NumSides['Rectangle'])                    # NumSides.Rectangle
print(NumSides['Square'])                       # NumSides.Rectangle

# __members__, list
print("----members, list----")

print(list(NumSides))           # -> Unique 위주
# [<NumSides.Triangle: 3>, <NumSides.Rectangle: 4>]

print(NumSides.__members__)     #  -> Alias 포함
# {'Triangle': <NumSides.Triangle: 3>, 'Rectangle': <NumSides.Rectangle: 4>, 'Square': <NumSides.Rectangle: 4>}


print(NumSides.__members__['Square'])

print("--------------------------------")
# [ Enumeration with Alias Sample ]

class Status(enum.Enum):
    ready = 'ready'

    running = 'running'
    busy = 'running'
    processing = 'running'


print(list(Status))
print(Status.__members__)
print(Status['busy'])
print(Status('running'))


print("--------------------------------")
# [ @enum.unique 로 Unqiue Value 보장하기 ]

try:
    @enum.unique
    class UniqueStatus(enum.Enum):
        ready = 1
        waiting = 1

        done_ok = 2
        errors = 3

except ValueError as e:
    print(e)        # duplicate values found in <enum 'UniqueStatus'>: waiting -> ready


@enum.unique
class UniqueStatus(enum.Enum):
    ready = 1
    # waiting = 1

    done_ok = 2
    errors = 3

# - OK
print(UniqueStatus.__members__)

