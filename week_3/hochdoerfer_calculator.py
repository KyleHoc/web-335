#----------------------------------------------------------
# Title: hochdoerfer_calculator.py
# Author: Kyle Hochdoerfer
# Date: 08/21/23
# Description: Code for calculating numerical values
#----------------------------------------------------------

#Declare a function for adding two parameters together
def add(x,y):
    #Return the sum of the parameters x and y
    return x + y

#Declare a function for subtracting one parameter from the other
def subtract(x,y):
    #Return the difference of the parameter y subtracted from x
    return x - y

#Declare a function for multiplying two parameters together
def multiply(x,y):
    #Return the product of x multiplied by y
    return x * y

#Declare a function for dividing two parameters
def divide(x,y):
    #Return the quotient of x divided by y
    return x / y


#Declare two integer variables for testing the calculation functions
num1 = 10
num2 = 5

#Call all four calculation functions, and store the results in string variables
add_result = str(num1) + " + " + str(num2) + " is " + str(add(num1, num2))
subtract_result = str(num1) + " - " + str(num2) + " is " + str(subtract(num1, num2))
multiply_result = str(num1) + " x " + str(num2) + " is " + str(multiply(num1, num2))
divide_result = str(num1) + " / " + str(num2) + " is " + str(divide(num1, num2))

#Print the calculation results variables to the console
print(add_result)
print(subtract_result)
print(multiply_result)
print(divide_result)