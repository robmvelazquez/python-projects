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