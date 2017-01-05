"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    num_input = raw_input("Enter your calculation: ")
    number_list = num_input.split(' ')
    if number_list[0] == "q":
        break
    else:
        if number_list[0] == "+":
            print add(number_list)
        elif number_list[0] == "-":
            print subtract(number_list)
        elif number_list[0] == "*":
            print multiply(number_list)
        elif number_list[0] == "/":
            print divide(number_list)
        elif number_list[0] == "square":
            print square(number_list)
        elif number_list[0] == "cube":
            print cube(number_list)
        elif number_list[0] == "power":
            print power(number_list)
        elif number_list[0] == "mod":
            print mod(number_list)
