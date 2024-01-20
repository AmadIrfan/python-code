# Lists in python
from pydoc import replace
import datetime

list = ["khan", "amad", "saad", ]
list1 = ['a', 'b', 'c', 'v']
list2 = [1, 3, 6, 2, 95, 4, 7]
list3 = [1.5, 3.6, 6.2, 2.4, 9.5, 4.0, 8.7, 7.1]
# list3.sort()
# for i in list3:
#     print(i)

#tuple in paython
tuple = ("khan", "amad", "saad", )
tuple1 = ('a', 'b', 'c', 'v')
tuple2 = (1, 3, 6, 2, 95, 4, 7)
tuple3 = (1.5, 3.6, 6.2, 2.4, 9.5, 4.0, 8.7, 7.1)

# Dictionary in python
# have a unique velue as "khan"
dict = {"khan": 1, "amad": 2, "saad": 3, "khan": 1}
dect1 = {"name": "John", "age": 36}
# dect1.
#set in python
# same as dictionary but different in velue
set = {"apple", "banana", "cherry"}

# multiLine string in python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# replace char in string
# print(a.replace("L","A"))

# list Extend
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

#functions in Python


def my_function(x, y):
    return 5 * x+y
# print(my_function(3, 1))
# print(my_function(5, 1))
# print(my_function(9, 2))


# using dateTime Modules
date = datetime.datetime.now()
print(date)
print(date.months)
