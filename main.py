import math

"""
Question 1: Printing the value of a string. 
"""


def q1_print(value):
    print(value)


"""
Question 2: 
Dynamic typing means there is no need to declare the type of the Variable whether it is Int or String or Other object.
Python interpreter will look at the provided value and would change the type of the variable.
As the type of the variable determined at the runtime (not at compile time), python is a Dynamic type language.
    * Pro's : 
        1)Its easy to write a code.
        2)We need less typing. 
        3) Easy to create a generic method.
        
    * Con's : 
        1) In a complex program it's may become difficult to debug. Which value causing what exception.
        2) There are possibilities to get runtime type conversion exception.       
"""


def q2_dynamic_typing():
    dynamic_variable = 12
    print('Type of the variable: %s value:%s' % (type(dynamic_variable), dynamic_variable))
    dynamic_variable = 'DynamicTyping'  # Dynamically the type of the is changed to String from Integer
    print('Type of the variable: %s value:%s' % (type(dynamic_variable), dynamic_variable))


"""
Question 3: Immutable objects are those which can not be modified once it's created. 
    For example String is a immutable object in Python.
"""


def q3_immutability():
    variable = 'StringIsImmutableSequence'
    print(variable[0])
    #   variable[0] = 'N'  # it will throw an exception.


"""
Question 4: Reversing the string using slicing. Negative index is used to track the string from the end. -1 means 
length -1 : which is the last character of the string. String slice has 3 component [start : end : step]. As i specified 
step as negative the default start value is -1 and then it will be stepped to (-1 -1 = -2) second last char so on. 
"""


def q4_string_reverse(param):
    print('%s -> After Reversing -> %s' % (param, param[::-1]))


"""
Question 5: Capitalizing a string will make the first character 'Capital' later. 
"""


def q5_capitalize(name):
    parts = name.split(' ')
    new_name = ''
    for part in parts:
        new_name = new_name + part.capitalize() + ' '
    print('Input: %s --> Output: %s' % (name, new_name))


"""
Question 6: Here the class coordinate is a blue print to hold any coordinate (x,y) in a plain.
whereas Objects are the physical copy of a class. Objects are been stored in memory. 
Class is there to help interpreter to create the object

Question 7:
Class or Objects are consists of 3 component i.e. 
    1) Variables which holds some value 
    2) Constructor which is used to create the objects.
    3) The functions/methods with does some action or evaluate something based on the data stored in variable.

"""


class Coordinate:
    # Variables
    x = 0
    y = 0

# Constructor
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

# Method
    def find_shortest_distance(self, coordinate=None):
        distance = (coordinate.y - self.y) ** 2 + (coordinate.x - self.x) ** 2
        return round(math.sqrt(distance), 2)


"""
Question 8: Printing alternating character using string slice [start : end : step]. Just specified the steps as 2 to 
skip one adjacent character.
"""


def q8_print_alternative(param):
    alt_string = param[0:len(param):2]
    print('%s is input --> Output is: %s' % (param, alt_string))


"""
Question 9: Division will always produce float value hence at the integer division we need to convert the float value to
int. That would loose the decimal point. for float division we don't need any conversion.   
"""


def q9_division(int1, int2):
    print('Integer division %d' % (int(int2 / int1)))
    print('Float division %.2f' % (int2 / int1))


"""
Question 10: Basically the concept is to get the sum of two value in one variable in order to get the value swapped.
(v1 + v2) - v2 = v1 & (v1 + v2) - v1 = v2, this is the trick used in the program. 
"""


def q10_swap_two_variable(int1, int2):
    print('Provided input:', int1, int2)
    int1 = int1 + int2
    int2 = int1 - int2
    int1 = int1 - int2
    print('After swapping output:', int1, int2)


if __name__ == '__main__':
    # Question 1.
    q1_print('The quick onyx goblin jumps over the lazy dwarf\'s head')
    # Question 2.
    q2_dynamic_typing()
    # Question 3.
    q3_immutability()
    # Question 4.
    q4_string_reverse('hello')
    # Question 5.
    q5_capitalize('david jones')
    # Question 6/ Question 7.
    start = Coordinate(1, 2)  # creating object of Coordinate class
    end = Coordinate(12, 20)
    print('Shortest distance between start and end :' + str(start.find_shortest_distance(end)))
    # Question 8.
    q8_print_alternative('MacBook')
    # Question 9.
    q9_division(12, 39)
    # Question 10.
    q10_swap_two_variable(15, 90)
