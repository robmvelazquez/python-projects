# this file has been used to test the commit and push functionality between PyCharm and GitHub.
# this file will be used for further miscellaneous tests down the line.
from collections import namedtuple

# These are examples of basic lists.
basic_list1 = [1, 2, 3, 4, 5]
basic_list2 = [1, "Two", 3, "Four", 5]
integers = "This is a list with only integers: "
str_and_int = "\nThis is a list with integers and strings: "

# To print the lists with a string, they must be concatenated.
# This can be accomplished with the .join method.
concatenated = integers + " ".join([str(item) for item in basic_list1])
concatenated2 = str_and_int + " ".join([str(item) for item in basic_list2])
print(concatenated)
print(concatenated2)

print("\nThis is a basic iterable.")
my_list1 = [1, 2, 3, 4, 5]
my_iterator = iter(my_list1)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# Point = namedtuple('Point', 'x,y')
# pt = Point(1, -4)
# print(pt.x, pt.y)
