import random
import secrets
import numpy as np

# Testing random with a random range
a = random.random()
print('Testing random with a random range: ' + str(a))

# Testing random with a specific range
a = random.uniform(1, 10)
print('Testing random with a specific range: ' + str(a))

# Testing random with an integer
a = random.randint(1, 10)
print('Testing random integer: ' + str(a))

# Testing a random range
a = random.randrange(1, 10)
print('Testing random with a random range: ' + str(a))

# Testing random with a value from a normal
a = random.normalvariate(0, 1)
print('Testing randow with a normal variate: : ' + str(a))

# Testing random with a random choice
mylist = list('ABCDEFGH')
a = random.choice(mylist)
print('Testing random with a random choice: ' + str(a))

# Testing random with a random unique choices
mylist = list('ABCDEFGH')
a = random.sample(mylist, 3)
print('Testing random with a random only unique choices: ' + str(a))

# Testing random with a random unique choices
mylist = list('ABCDEFGH')
a = random.choices(mylist, k=3)
print('Testing random with possible duplicate choices: ' + str(a))

# Testing the random shuffle method
mylist = list('ABCDEFGH')
random.shuffle(mylist)
print('Testing the random shuffle method: ' + str(mylist))

# Testing with the random seed method
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))

# Testing random with secrets - 1111 = 16 binary bits
a = secrets.randbits(4)
print('Testing random with secrets to find a number between 1-16: ' + str(a))

# Testing random with secrets
mylist = list('ABCDEFGH')
a = secrets.choice(mylist)
print('Testing random with secrets: ' + str(a))

# Testing random with numpy
a = np.random.rand(3, 3)
print('Testing random with numpy: ' + str(a))

# Testing random integers in an array
a = np.random.randint(0, 10, 3) # (0, 10) is the range with '10' being excluded. '3' is the size.
print('Testing random integers in an array: ' + str(a))

# Testing random integers in an array with higher dimensions
# (0, 10) is the range with '10' being excluded. The (3, 4) tuple increases the dimensions
a = np.random.randint(0, 10, (3, 4))
print('Testing random integers in an array: ' + str(a))

# Testing random shuffle with an array. This will shuffle only the first list in the array.
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('Testing random shuffle with an array\n' + str(arr))
np.random.shuffle(arr)
print(arr)

# Testing numpy random seed method

np.random.seed(1)
print('Testing random seed method with numpy\n' + str(np.random.rand(3,3)))
np.random.seed(1)
print(np.random.rand(3,3))

