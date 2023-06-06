import sys
def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()

# This can be used to print each yield of the generator
# for i in g:
#    print(i)

""" These lines of code can be used to iterate each yield of the generator individually
value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)
"""

# This can print the sum of the yield in the generator
# print(sum(g))

# This can sort the yields within the generator
# print(sorted(g))

# This generator iterates each value within a countdown function
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)

value = next(cd)
print(value)

print(next(cd))
print(next(cd))
print(next(cd))

# This function outputs a normal function and a generator.
# It demonstrates the efficiency of generators and how much space they save:
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(f'These are the elements within {firstn.__name__}: {firstn(10)}')
print(f'This is the sum of {firstn.__name__}: {sum(firstn(10))}')
print(f'This is the sum of {firstn_generator.__name__}: {sum(firstn_generator(10))}')

print(f'This is the size of {firstn.__name__}: {sys.getsizeof(firstn(100))}')
print(f'This is the size of {firstn_generator.__name__}:  {sys.getsizeof(firstn_generator(100))}')

# This generator is used to output the Fibonnaci sequence,
# which calculates each number as the sum of the preceding numbers.
def fibonacci(limit):
    # 0 1 1 2 3 5 8 13 ...
    a, b = 0, 1
    while a < limit:
        yield  a
        a, b = b, a + b

fib = fibonacci(100)
for i in fib:
    print(i)

# These lines of code help explain the difference in size between a generator and a list.
mygenerator = (i for i in range(100000) if i % 2 == 0)
print(f'This is the size of mygenerator: {sys.getsizeof(mygenerator)}')

mylist = [i for i in range(100000) if i % 2 == 0]
print(f'This is the size of mylist: {sys.getsizeof(mylist)}')