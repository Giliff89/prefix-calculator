def add(number_list):
    """Return the sum of some numbers"""
    subtotal = 0
    for number in number_list:
        if number == number_list[0]:
            pass
        else:
            new_num = int(number)
            subtotal += new_num
    return subtotal


def subtract(number_list):
    """Return the difference of two numbers"""
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
    """Return the product of two numbers"""
    for number in number_list:
        if number == number_list[0]:
            pass
        elif number == number_list[1]:
            new_num = float(number)
        else:
            new_num *= float(number)
    return new_num


def divide(number_list):
    """Return the quotient of two numbers as a float"""
    for number in number_list:
        if number == number_list[0]:
            pass
        elif number == number_list[1]:
            new_num = float(number)
        else:
            new_num /= float(number)
    return new_num


def square(num):
    """Return the square of a number"""
    return power(num, 2)


def cube(num):
    """Return the cube of a number"""
    return power(num, 3)


def power(num, exponent):
    """Return num raised to the power of exponent"""
    return float(num) ** exponent


def mod(num1, num2):
    """Return remainder of num1 divided by num2"""
    return num1 % num2
