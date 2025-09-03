#!usr/bin/env python3

# # print hello world sample
# print('hello world')
# print("Hello' 'world")

# #JSON Format
# print('{"message":"JSON Format"}')
# print("{\"message\":\"JSON Format\"}")

# # declaring a variable
# value = 10
# # sum = value + 20
# # print(sum)

# # defining a list
# values = [10, 25, 5 -3]

# # print sum - using python built in sum function
# print( f'Sum = { sum( values ) }' )

# # Conditionals - different ways to  check conditionals
# condition_val = 1
# # if conditional_val:
# # if conditional_val == 1:
# # if conditional_val == True:
#     # print( 'True' )

# # True -> anything above 0 or False. Unless you use == operator
# condition_val = 2

# if condition_val:
#     print( 'True' )

# # Else if - multiple conditions
# conditional_2 = 3
# if conditional_2 == 2:
#     print( 'Condition is:', conditional_2)
# elif conditional_2 == 3:
#     print( 'Condition is:', conditional_2)
# else:
#     print( 'Condition is neither 2 or 3' )

# #----------------------------------------------------------------#
# # Python Types | Data Structures #
# integer_type = 5
# float_type = 5.0
# string_type = str(5)

# print( type(integer_type) )
# print( type(float_type) )
# print( type(string_type) )

# # Use type function to check object's data type
# if type( integer_type ) == type ( int() ):
#     print( 'Its an integer' )

# # plus additional data structures -> lists, tuples, dictionaries, sets

# # lists() - a collection of objects. Objects need not be of same type
# list_variable = [1, 3, 4, 10]
# print( type( list_variable ) )
# print( 'list_variable : ', list_variable )

# list_variable = [1, "string", 3.141, 11]
# print( 'New list_variable : ', list_variable )

# # indexes in python start from 0
# print( list_variable[1] )

# # multiplying the list elements will  not mathematically multiply
# # but rather will display elements multiple times
# print( 2*list_variable )

# # different ways to define list - and you can add values to them
# list1 = []
# list2 = list()

# List Methods
# append - Adds an element at the end of the list
# clear() - Removes all the elements from the list
# copy() - Returns a copy of the list
# count() - Returns the number 

#----------------------------------------------------------------------#
# Tuples - 

# Defining a tuple
# tuple_variable1 = (2, 3)
# print( tuple_variable1 )

# # Tuples can be converted from lists and vice-versa
# tuple_variable2 = tuple([3, 4, 5])
# print( tuple_variable2 )
# print( type( tuple_variable1 ) )

# # unpacking tuples
# value_1, value_2 = tuple_variable1
# print( 'Value 1:', value_1 )
# print( 'Value 2:', value_2 )

# ---------------------------------------------------------------------#
# Dictionaries - used key:value pairs
# Dictionaries are not indexed by numbers
# Must use index by key

# dictionary_variable1 =  dict()
# dictionary_variable2 = {}
# dictionary_variable3 = {"key_1" : "value_1"}
# print(dictionary_variable3)

# print(dictionary_variable3['key_1'])

# dictionary_variable4 = { "key_1" : [1, 5, "value", 4.0]}
# print(dictionary_variable4)

# Dictionay Methods
# 1. 

#--------------------------------------------------------------------------#
# Sets - cannot have duplicate items

# set_variable = set()

# Set - Methods

#---------------------------------------------------------------------------#
# Range function
# print( range(6) )
# print( range(1, 5) )
# print( len(range(2, 10)) )
# print( range(1, 10, 2) )

# Loops
list1 = [1, 2, 3, 4, 5, 6, 7]

# using the range
# for index in range( len(list1) ):
#     print( index, list1[index] )

# using the 'in' keyword
# for item in list1:
#     print( item )

# using enumerate - return the range count and the item
# for index, item in enumerate(list1):
#     print(index, item)

# range is inclusive at start, not at the end
# for odd in range(1, 10, 2):
#     print( odd )

# for even in range(0, 10, 2):
#     print( even )

# -----------------------------------------------------------#
# While Loops

# while_condition = 0
# while while_condition < 6:
#     while_condition += 1
#     print(while_condition)
# else:
#     print( 'While Loop ended now.' )


#------------------------------------------------------------#
# Math Operators
# +, -, *, /, %, **

# Logic Operators
# ==, !=, >, >=, <. <=

# Assignment Operators
# +=, -=, *=, /=, %=, &=, |=, ^=, ~=,

# Logical Operators
# and, or, not

# Identity Operators
# is - Return True if both variables are the same object, x is y
# is not - Returns True of both variables are not the same object, x is not y

# Membership Operators
# in - Return True if a specified object is present in the sequence
# not in - Return True if a specified object is not present in the sequence

# Bitwise Operators
# & :- AND
# | :-  OR
# ^ :- XOR
# ~ :- NOT
# << :- Zero fill left shift
# >> Signed right shift

#--------------------------------------------------------------------------#