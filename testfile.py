import collections
import functools
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



# another example of using the groupby function but with age.
print("\nUsing the groupby function to group elements by age.")
persons = [{'name': 'Rob', 'age': 25}, {'name': 'Micah', 'age': 25},
           {'name': 'Tali', 'age': 27}, {'name': 'Veronica', 'age': 24}]

group_obj1 = itertools.groupby(persons, key=lambda x: x['age'])
for key, value in group_obj1:
    print(key, list(value))



# count function
print("\nThis is an example of the count function.")
for i in itertools.count(10):
    print(i)
    if i == 15:
        break



""" This is an example of the cycle function. It will continue to loop forever, because
it is an infinite iterator.
a = [1, 2, 3]
for i in itertools.cycle(a):
    print(i)



This is an example of the repeat function. It will continue to loop forever, unless given an
escape argument. """
print("\nThis is an example of the repeat function.")
a = [1, 2, 3]
for i in itertools.repeat(1, 4):
    print(i)



"""
Here's the general syntax of a lambda function: 
lambda parameter: expression

Instead of creating a standard function such as this one:
def multiply(x, y):
    return x * y
print(multiply(3,4))    
    
We can use a lambda function such as the one below to generate a simple,
anonymous, concise, readable function that reduces complexity.
"""
print("\nThis is an example of a lambda function.")
multiply_lambda = lambda x, y: x * y
print(multiply_lambda(3,4))



print("\nThis sorted lambda function will sort the tuples by their 'y' values.")
points2d = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2d_sorted = sorted(points2d, key=lambda x: x[1])
print(points2d)
print(points2d_sorted)


print("\n# this sorted lambda function will sort by the sum of each tuple.")
points2d = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2d_sorted = sorted(points2d, key=lambda x: x[0] + x[1])
print(points2d)
print(points2d_sorted)



# The map function is used to apply a specific function to each item of an iterable.
# map syntax == map(function, iterable)
print("\nThis is an example of using the map function to double a number.")
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(a))
print(list(b))



print("\nThis is another example of using the map function to double a number.")
# Define a function to double a number using the map function.
def double(x):
    return x * 2

# Apply the 'double' function to each element in the list.
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(double, numbers)

for num in doubled_numbers:
    print(num)



print("\nThis is a method to double list(a) without using the map lambda function.")
c = [x*2 for x in a]
print(c)



# The filter function is used to apply a given function to each element in an iterable.
# filter syntax == filter(function, iterable)
print("\nThis is an example of the filter function.")
a = [1, 2, 3, 4, 5, 6]
# the % symbol represents the modulus operator that calculates the remainder.
# in this example, x%2==0 means that if x / 2 = remainder 0, then the condition is True.
b = filter(lambda x: x%2==0, a)
print(list(b))

print("\nThis is a method to filter without using the filter lambda function.")
c = [x for x in a if x%2==0]
print(c)


"""
The reduce function is used to apply a function to a sequence of elements and reduce
sequence to a single value.
reduce syntax == reduce(function, iterable) 
"""
a = [1, 2, 3, 4]
product_a = functools.reduce(lambda x, y: x*y, a)
print("\nThis is an example of the reduce function: " + str(product_a))