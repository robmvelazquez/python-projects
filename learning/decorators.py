import functools
"""
Decorators are used to extend the behavior of a function.
Below is the structure template of a decorator:

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before initial function
        # Calling initial function
        # Do something after initial function
        return result
    return wrapper

@my_decorator
def random_func():
    return a + b
"""

# This decorator is used to print 'Start', the contents of the func, and 'End'
def start_end_decorator(func):
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper
@start_end_decorator
def print_name():
    print('Rob')

print_name()

# This function extends the greet function by implementing a repeat function.
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature}")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper
@debug
@repeat(num_times=4)
def greet(name):
    print(f'Hello {name}')

greet('Rob')

# This function will output 'Start', 'End', and the result of the add function.
def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper
@start_end_decorator
def add5(x):
    return x + 5

result = add5(10)
print(result)

# The CountCalls function will output the # of times the say_hello() func is executed.
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
   print('Hello')

say_hello()
say_hello()