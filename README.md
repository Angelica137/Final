# These are my solutions to some very important problems

## Problem 3

Numbers in Mandarin follow 3 simple rules.

There are words for each of the digits from 0 to 10.
For numbers 11-19, the number is pronounced as "ten digit", so for example, 16 would be pronounced (using Mandarin) as "ten six".
For numbers between 20 and 99, the number is pronounced as “digit ten digit”, so for example, 37 would be pronounced (using Mandarin) as "three ten seven". If the digit is a zero, it is not included.
Here is a simple Python dictionary that captures the numbers between 0 and 10.

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
'5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
We want to write a procedure that converts an American number (between 0 and 99), written as a string, into the equivalent Mandarin.

def convert_to_mandarin(us_num):
'''
us_num, a string representing a US number 0 to 99
returns the string mandarin representation of us_num
''' # FILL IN YOUR CODE HERE
Example Usage

convert_to_mandarin('36') will return san shi liu
convert_to_mandarin('20') will return er shi
convert_to_mandarin('16') will return shi liu

## Problem 4

You are given the following definitions:

A run of monotonically increasing numbers means that a number at position k+1 in the sequence is greater than or equal to the number at position k in the sequence.
A run of monotonically decreasing numbers means that a number at position k+1 in the sequence is less than or equal to the number at position k in the sequence.
Implement a function that meets the specifications below.

def longest_run(L):
"""
Assumes L is a list of integers containing at least 2 elements.
Finds the longest run of numbers in L, where the longest run can
either be monotonically increasing or monotonically decreasing.
In case of a tie for the longest run, choose the longest run
that occurs first.
Does not modify the list.
Returns the sum of the longest run.
""" # Your code here
For example:

If L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2] then the longest run of monotonically increasing numbers in L is [3, 4, 5, 7, 7] and the longest run of monotonically decreasing numbers in L is [10, 4, 3]. Your function should return the value 26 because the longest run of monotonically increasing integers is longer than the longest run of monotonically decreasing numbers.
If L = [5, 4, 10] then the longest run of monotonically increasing numbers in L is [4, 10] and the longest run of monotonically decreasing numbers in L is [5, 4]. Your function should return the value 9 because the longest run of monotonically decreasing integers occurs before the longest run of monotonically increasing numbers.

Problem 5
0.0/20.0 points (graded)
Assume you are given two dictionaries d1 and d2, each with integer keys and integer values. You are also given a function f, that takes in two integers, performs an unknown operation on them, and returns a value.

Write a function called dict_interdiff that takes in two dictionaries (d1 and d2). The function will return a tuple of two dictionaries: a dictionary of the intersect of d1 and d2 and a dictionary of the difference of d1 and d2, calculated as follows:

intersect: The keys to the intersect dictionary are keys that are common in both d1 and d2. To get the values of the intersect dictionary, look at the common keys in d1 and d2 and apply the function f to these keys' values -- the value of the common key in d1 is the first parameter to the function and the value of the common key in d2 is the second parameter to the function. Do not implement f inside your dict_interdiff code -- assume it is defined outside.
difference: a key-value pair in the difference dictionary is (a) every key-value pair in d1 whose key appears only in d1 and not in d2 and (b) every key-value pair in d2 whose key appears only in d2 and not in d1.
Here are two examples:

If f(a, b) returns a + b
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
If f(a, b) returns a > b
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})
def dict_interdiff(d1, d2):
'''
d1, d2: dicts whose keys and values are integers
Returns a tuple of dictionaries according to the instructions above
''' # Your code here

Problem 6
0.0/20.0 points (graded)
In this problem, you will implement a class according to the specifications in the template file usresident.py. The file contains a Person class similar to what you have seen in lecture and a USResident class (a subclass of Person). Person is already implemented for you and you will have to implement two methods of USResident.

For example, the following code:

a = USResident('Tim Beaver', 'citizen')
print(a.getStatus())
b = USResident('Tim Horton', 'non-resident')
will print out:

citizen

## will show that a ValueError was raised at a particular line

usresident.py

## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS

class Person(object):
def **init**(self, name):
#create a person with name name
self.name = name
try:
firstBlank = name.rindex(' ')
self.lastName = name[firstBlank+1:]
except:
self.lastName = name
self.age = None
def getLastName(self):
#return self's last name
return self.lastName
def setAge(self, age):
#assumes age is an int greater than 0
#sets self's age to age (in years)
self.age = age
def getAge(self):
#assumes that self's age has been set
#returns self's current age in years
if self.age == None:
raise ValueError
return self.age
def **lt**(self, other):
#return True if self's name is lexicographically less
#than other's name, and False otherwise
if self.lastName == other.lastName:
return self.name < other.name
return self.lastName < other.lastName
def **str**(self):
#return self's name
return self.name

class USResident(Person):
"""
A Person who resides in the US.
"""
def **init**(self, name, status):
"""
Initializes a Person object. A USResident object inherits
from Person and has one additional attribute:
status: a string, one of "citizen", "legal_resident", "illegal_resident"
Raises a ValueError if status is not one of those 3 strings
""" # Write your code here

def getStatus(self):
"""
Returns the status
""" # Write your code here

Problem 7
0.0/20.0 points (graded)
You are given the following superclass. Do not modify this.

class Container(object):
""" Holds hashable objects. Objects may occur 0 or more times """
def **init**(self):
""" Creates a new container with no objects in it. I.e., any object
occurs 0 times in self. """
self.vals = {}
def insert(self, e):
""" assumes e is hashable
Increases the number times e occurs in self by 1. """
try:
self.vals[e] += 1
except:
self.vals[e] = 1
def **str**(self):
s = ""
for i in sorted(self.vals.keys()):
if self.vals[i] != 0:
s += str(i)+":"+str(self.vals[i])+"\n"
return s
Write a class that implements the specifications below. Do not override any methods of Container.

class ASet(Container):
def remove(self, e):
"""assumes e is hashable
removes e from self""" # write code here

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        # write code here

For example,
d1 = ASet()
d1.insert(4)
d1.insert(4)

d1.remove(2)
print(d1)

d1.remove(4)
print(d1)
prints
4:2 # from d1.remove(2) print

    # (empty) from d1.remove(4) print

For example,
d1 = ASet()
d1.insert(4)
print(d1.is_in(4))
d1.insert(5)
print(d1.is_in(5))
d1.remove(5)
print(d1.is_in(5))
prints
True
True
False
Paste your entire class in the box below. Do not leave any debugging print statements.
