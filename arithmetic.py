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


def subtract(num1, num2):
    """Return the difference of two numbers"""
    return num1 - num2


def multiply(num1, num2):
    """Return the product of two numbers"""
    return num1 * num2


def divide(num1, num2):
    """Return the quotient of two numbers as a float"""
    return float(num1) / num2


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
