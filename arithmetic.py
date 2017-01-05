def add(number_list):
    """Return the sum of s series of numbers"""
    subtotal = 0
    for number in number_list:
        if number == number_list[0]:
            pass
        else:
            new_num = int(number)
            subtotal += new_num
    return subtotal


def subtract(number_list):
    """Return the difference of a series numbers"""
    subtotal = 0
    for number in number_list:
        if number == number_list[0]:
            pass
        elif number == number_list[1]:
            subtotal = int(number)
        else:
            new_num = int(number)
            subtotal -= new_num
    return subtotal


def multiply(number_list):
    """Return the product of a series of numbers"""
    for number in number_list:
        if number == number_list[0]:
            pass
        elif number == number_list[1]:
            new_num = float(number)
        else:
            new_num *= float(number)
    return new_num


def divide(number_list):
    """Return the quotient of a series of numbers as a float"""
    for number in number_list:
        if number == number_list[0]:
            pass
        elif number == number_list[1]:
            new_num = float(number)
        else:
            new_num /= float(number)
    return new_num


def square(number_list):
    """Return the square of a series of numbers"""
    squared = ''
    for number in number_list:
        if number == number_list[0]:
            pass
        else:
            new_num = float(number)
            new_num **= 2
            squared += '%d ' % new_num
    return squared


def cube(number_list):
    """Return the cube of a series of numbers"""
    cubed = ''
    for number in number_list:
        if number == number_list[0]:
            pass
        else:
            new_num = float(number)
            new_num **= 3
            cubed += '%d ' % new_num
    return cubed


def power(number_list):
    """Return numbers raised to the power of exponent"""
    for number in number_list:
        if number == number_list[0]:
            pass
        elif number == number_list[1]:
            new_num = float(number)
            print new_num
        else:
            new_num **= float(number)
            print new_num
    return new_num


def mod(number_list):
    """Return remainder of number 1 divided by number 2"""
    return float(number_list[1]) % float(number_list[2])
