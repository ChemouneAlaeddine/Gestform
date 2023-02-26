import random

# The maximum & minimum values of our integers
MAX_INTEGER_VALUE = 1000
MIN_INTEGER_VALUE = -1000

# The first and the second divisor
FIRST_DIV_NUM = 3
SECOND_DIV_NUM = 5

# The minimum length of our list
MIN_LIST_LENGTH = 1

def input_list_length(min_int, max_int):
    """
    input_list_length asks for an integer from the user.
    :Param 1: The minimum value accepted of the input integer
    :Param 2: The maximum value accepted of the input integer
    :return: An integer between 1 and 2000
    """ 
    while True:
        try:
            input_integer = int(input("Enter the length of the list : "))
        except ValueError:
            print("Please input integer only...")
            continue
        if (input_integer < min_int or input_integer > max_int):
            print("the list length should be between {} and {}".format(min_int, max_int))
            continue
        break
    return input_integer


if __name__ == "__main__":
    # The interval of the list of integers
    integer_list = [item for item in range(MIN_INTEGER_VALUE, MAX_INTEGER_VALUE)]

    # Input the length of the list of integers (It should be between 1 and the integer_list length)
    list_length = input_list_length(MIN_LIST_LENGTH, integer_list.__len__())

    # Creation of the random list
    list_values = random.sample(integer_list, list_length)

    # Sorting the created list
    list_values.sort()

    # Display of the created list
    print("The created list is : {}".format(list_values))

    # Browse the list
    for var in list_values:
        if ((var % FIRST_DIV_NUM == 0) and (var % SECOND_DIV_NUM == 0)): # Write Gestform
            print("{} : Gestform".format(var))
        elif (var % FIRST_DIV_NUM == 0): # Write Geste
            print("{} : Geste".format(var))
        elif (var % SECOND_DIV_NUM == 0): # Write Forme
            print("{} : Forme".format(var))
        else:
            print(var)

