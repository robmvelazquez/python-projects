from multiprocessing import Pool


# This program will cube every number within the range (0-9)
def cube(number):  # Defines the cube function with argument 'number'
    return number * number * number


if __name__ == "__main__":

    numbers = range(10)  # Creates a list of numbers '0-9' using variable 'numbers'
    pool = Pool()

    # map, apply, join, close
    result = pool.map(cube, numbers)  # The 'map' method applies the cube function to each number in list 'numbers'
    # pool.apply(cube, numbers[0])

    pool.close()
    pool.join()

    print(result)
