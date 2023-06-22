"""
Recursive factorial function finds the factorial of an integer. Recursive functions develop 
clean code and break down a complex task into simple sub-problems. However, recursive calls are
inefficient and difficult to debug.
"""


def factorial(x):

  if x == 1:
      return 1  # This is the base condition which ends the function.
  else:
      return (x * factorial(x-1))

num = 3
print("The factorial of", num, "is", factorial(num))
  
