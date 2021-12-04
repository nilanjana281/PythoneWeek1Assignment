import math


def q1_print(value):
    # Assignment Q1.
    print(value)  # Press Ctrl+F8 to toggle the breakpoint.


def q2_dynamic_typing():
    # Dynamic typing means there is no need to declare the type of the Variable whether it is Integer or String or
    # Other object. Python interpreter will look at the provided value and would change the type of the variable.
    # As the type of the variable determined at the runtime (not at compile time).
    # That is why python is a Dynamic type language.
    # Pro's : Its easy to write a code. We need less typing. Easy to create a generic method.
    # Con's : In a complex program it's difficult to debug if some value producing any exception in runtime.
    dynamic_variable = 12
    print('Type of the variable: %s value:%s' % (type(dynamic_variable), dynamic_variable))
    dynamic_variable = 'DynamicTyping'  # Dynamically the type of the is changed to String from Integer
    print('Type of the variable: %s value:%s' % (type(dynamic_variable), dynamic_variable))


def q3_immutability():
    # Immutable objects are those which can not be modified once its created.
    # For example String is a immutable object in Python.
    variable = 'StringIsImmutableSequence'
    print(variable[0])
    #   variable[0] = 'N'  # it will throw an exception.


def q4_string_reverse(param):
    print('%s -> After Reversing -> %s' % (param, param[::-1]))


def q5_capitalize(name):
    parts = name.split(' ')
    new_name = ''
    for part in parts:
        new_name = new_name + part.capitalize() + ' '
    print('Input: %s --> Output: %s' % (name, new_name))


# Here the class coordinate is a blue print of (x,y) coordinate in a plain. It consists of two component
# The components of a Class are variables with holds some value and the functions with does some action.
# Object is the physical copy of a class. Objects are been stored in memory.
# Class is there to help interpreter to create the object.

class Coordinate:
    x = 0
    y = 0

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def find_shortest_distance(self, coordinate=None):
        distance = (coordinate.y - self.y) ** 2 + (coordinate.x - self.x) ** 2
        return round(math.sqrt(distance), 2)


if __name__ == '__main__':
    # Assignment Q1.
    q1_print('The quick onyx goblin jumps over the lazy dwarf\'s head')
    q2_dynamic_typing()
    q3_immutability()
    q4_string_reverse('hello')
    q5_capitalize('david jones')

    # Q6
    start = Coordinate(1, 2)  # creating object of Coordinate class
    end = Coordinate(12, 20)
    print('Shortest distance between start and end :' + str(start.find_shortest_distance(end)))
