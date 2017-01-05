"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    calculation = raw_input("Enter your calculation: ")
#    print calculation
    value_list = calculation.split(' ')
#    print value_list
    if value_list[0] == "q":
        break
    else:
        if value_list[0] == "+":
            print add(int(value_list[1]), int(value_list[2]))
        elif value_list[0] == "-":
            print subtract(int(value_list[1]), int(value_list[2]))
        elif value_list[0] == "*":
            print multiply(int(value_list[1]), int(value_list[2]))
        elif value_list[0] == "/":
            print divide(int(value_list[1]), int(value_list[2]))
