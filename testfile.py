import collections
import functools
import itertools

# These are examples of basic lists.
basic_list1 = [1, 2, 3, 4, 5]
basic_list2 = [1, "Two", 3, "Four", 5]
integers = "This is a list with only integers: "
str_and_int = "\nThis is a list with integers and strings: "

# To print the lists with a string, they must be concatenated. This can be accomplished with the .join method.
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
Point = collections.namedtuple('Point', 'x,y')
pt = Point(1, -4)
print("\nThis is an example of a namedtuple.\n" + str(pt.x) + ", " + str(pt.y))



# permutations output all possible arrangements of elements within an iterable.
# permutations is a function from the itertools module.
permutations = itertools.permutations(my_list1)
print("\nThis is an example of permutations.")
for perm in permutations:
    print(perm)



# combinations output all possible combinations of elements within an iterable.
# combinations requires two arguments: the iterable and the length.
comb = itertools.combinations(my_list1, 2)
print("\nThis is an example of combinations.\n" + str(list(comb)))



# combinations with replacements outputs the combinations of each element to include itself.
comb_wr = itertools.combinations_with_replacement(my_list1, 2)
print("\nThis is an example of combinations with replacements.\n" + str(list(comb_wr)))



# accumulate will calculate the sum of the elements.
acc = itertools.accumulate(my_list1)
print("\nThis is an example of the accumulate function.\n" + str(my_list1) + "\n" + str(list(acc)))



# groupby will group elements based on specific given criteria.
print("\nThis is an example of using the groupby function to determine if a number is <= 3.")
def smaller_than_3(x):
    return x < 3
group_obj = itertools.groupby(my_list1, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))



# another example of using the groupby function but with age.
persons = [{'name': 'Rob', 'age': 25}, {'name': 'Micah', 'age': 25},
           {'name': 'Tali', 'age': 27}, {'name': 'Veronica', 'age': 24}]
print("\nThis is an example of using the groupby function to group elements by age.")

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
a = [1, 2, 3]
print("\nThis is an example of the repeat function.")
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
multiply_lambda = lambda x, y: x * y
print("\nThis is an example of a lambda function.\n" + str(multiply_lambda(3,4)))



points2d = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2d_sorted = sorted(points2d, key=lambda x: x[1])
print("\nThis sorted lambda function will sort the tuples by their 'y' values.\n" + str(points2d))
print(points2d_sorted)


points2d = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2d_sorted = sorted(points2d, key=lambda x: x[0] + x[1])
print("\nThis sorted lambda function will sort by the sum of each tuple.\n" + str(points2d))
print(points2d_sorted)


"""
The map function is used to apply a specific function to each item of an iterable.
map syntax == map(function, iterable)
"""
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print("\nThis is an example of using the map function to double a number.\n" + str(list(a)))
print(list(b))



# This is another map example that defines a function to double a number.
def double(x):
    return x * 2

# Apply the 'double' function to each element in the list.
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(double, numbers)
print("\nThis is another example of using the map function to double a number.")

for num in doubled_numbers:
    print(num)



c = [x*2 for x in a]
print("\nThis is a method to double list(a) without using the map lambda function.\n" +str(c))


"""
The filter function is used to apply a given function to each element in an iterable.
filter syntax == filter(function, iterable)
the % symbol represents the modulus operator that calculates the remainder.
in this example, x%2==0 means that if x / 2 = remainder 0, then the condition is True.
"""
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x%2==0, a)
print("\nThis is an example of the filter function.\n" + str(list(b)))

c = [x for x in a if x%2==0]
print("\nThis is a method to filter without using the filter lambda function.\n" + str(c))


"""
The reduce function is used to apply a function to a sequence of elements and reduce
sequence to a single value.
reduce syntax == reduce(function, iterable) 
"""
a = [1, 2, 3, 4]
product_a = functools.reduce(lambda x, y: x*y, a)
print("\nThis is an example of the reduce function: \n" + str(product_a))


""" ===== Errors and Exceptions =====

TypeError
    x = 5
    y = "Hello, world!"
    result = x + y
    print(result) # cannot concatenate a string and an integer this way

# ModuleNotFoundError
    import somemodule # Invalid module name

# SyntaxError
    a = 5
    print(a)) # Too many parenthesis

# NameError
    a = 5
    b = c # variable 'c' is not defined

# FileNotFoundError
    f = open('somefile.txt') # file does not exist

# ValueError
    a = [1,2,3]
    a.remove(4) # '4' is an invalid value

# IndexError
    a = [1,2,3]
    a[4]
    print(a) # '4' is an invalid index

# KeyError
    my_dict = {'name': 'Max'}
    my_dict['age'] # key 'age' is an invalid key

# Raise an Exception when false
    x = -5
    if x < 0:
        raise Exception('x should be positive')
    
    # Utilize the Assert statement to throw an error when false
    x = -5
    assert (x>=0), 'x is not positive'

# Try/Except
    try:
        a = 5 / 0
    except:
        print('An error has occured.')
    
    # Print the exception
    try:
        a = 5 / 0
    except Exception as e:
        print(e)
    else:
        print('No errors detected.')
    finally: # finally clause always runs no matter the outcome.
        print('cleaning up...')

# Defining an error
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high.')
    if x < 5:
        raise ValueTooSmallError('Value is too small.', x)

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)

"""
