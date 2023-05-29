import collections
from collections import namedtuple
import itertools


# this file has been used to test the commit and push functionality between PyCharm and GitHub.
# this file will be used for further miscellaneous tests down the line.


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


# Each time an iterator is called, it returns the next element.
print("\nThis is a basic iterable.")
my_list1 = [1, 2, 3, 4]
my_iterator = iter(my_list1)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))


# namedtuple is a function from the collections module.
print("\nThis is an example of a namedtuple.")
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt.x, pt.y)


# permutations output all possible arrangements of elements within an iterable.
# permutations is a function from the itertools module.
permutations = itertools.permutations(my_list1)
print("\nThis is an example of permutations.")
for perm in permutations:
    print(perm)


# combinations output all possible combinations of elements within an iterable.
# combinations requires two arguments: the iterable and the length.
comb = itertools.combinations(my_list1, 2)
print("\nThis is an example of combinations.")
print(list(comb))


# combinations with replacements outputs the combinations of each element
# to include itself.
comb_wr = itertools.combinations_with_replacement(my_list1, 2)
print("\nThis is an example of combinations with replacements.")
print(list(comb_wr))


# accumulate will calculate the sum of the elements.
acc = itertools.accumulate(my_list1)
print("\nThis is an example of the accumulate function.")
print(my_list1)
print(list(acc))


# groupby will group elements based on specific given criteria.
print("\nThis is an example of the groupby function.")
def smaller_than_3(x):
    return x < 3
group_obj = itertools.groupby(my_list1, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

