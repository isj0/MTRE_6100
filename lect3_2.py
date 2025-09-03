#!usr/bin/env python3

# Dunder or magic methods - double underscores, __name__, __init__

# Functions - definitions

def method():
    # pass keyword allows you to skip this line of code
    pass
    # continue allws you to skip an iterator in a loop

#method declaration with paramter not set
def method_2():
    print()

#method declaration with paramter preset
def method_3(param1=None):
    print(param1)

def method_4(param1 = 0, param2 = 1):
    print("param1:", param1)
    print("param2:", param2)

# variable argument passing
def method_arg(*arg):
    print(arg)

# variable number of argument passing with keys
def method_kwarg(**kwarg):
    print(kwarg)

def binary_hex():
    string = 'a'
    #ord = python method for converting char to int
    int_value = ord(string[0])  # this value should match the ascii table
    print('int_value', int_value)
    # str() - python type for strings
    encoded_variable = str.encode(string)
    print(encoded_variable)
    print(encoded_variable[0])
    print(encoded_variable.decode)
    print(chr(97))      # type casting
    print( hex(int_value) )
    print( bin(int_value) )
    #int (what, base) - base 16 = hex
    print( int(string[0], 16) )
    print( hex( int(string[0], 16) ) )
    # hex = 0-9, A-F

global_variable = 20
def global_values():
    # global keyword is needed to utilize the globally declared object
    # global global_variable
    # print('global_variable from the method global_values before assignment:', global_variable)
    # this is reasignment- will make it a local variable and no lionger references it
    global_variable = 10
    print('global_variable from the method global_values after assignment:', global_variable)

def colon_operator():
    list_variable = [1, 2, 4, 5, 6, 7, 8, 9]
    #start:stop:step_size
    # start is inclusive, stop is exclusive
    print( list_variable[0:3] )
    print( list_variable[2:4] )
    print( list_variable[2:6:2] )
    print( list_variable[-1] )
    print( list_variable[-1:-4:-1] )

def lambda_functions(n = 2):
    doubler = lambda param1: param1*param1
    print( doubler(2) )
    multiplier = lambda param1, param2: param1 * param2
    print( multiplier(2,3) )
    filter_even = lambda input_list: input_list % 2 == 0
    filtered = ( filter(filter_even, [1,2,3,4,5,6,7,8,9] ) )
    print( list(filtered) ) 
    return lambda x: x**n



def main():
    print('This is our main program')
    method()
    method_2()
    # this will cause an error- parameter missing
    method_2()     
    # predefining value for your parameter allows you to not pass one in
    method_3()
    method_4()
    method_4(param2 = 3)
    method_4(2, 4)
    method_arg(1, 2, 3, 4, 5)
    # kwargs are used in machine learning passing models and datasets.
    method_kwarg(key_1 = 1, key_2 = 2)
    binary_hex()
    print('global variable', global_variable)
    global_values()     # global variable in the method will be printed
    print('global variable', global_variable)
    colon_operator()
    lambda_functions()
    doubler = lambda_functions(n = 2)
    print(doubler(2))
    tripler = lambda_functions( n = 3)
    print(tripler(2))




if __name__ == "__main__":
    main()
