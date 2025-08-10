def add(a, b):
    """Add two number

    Args:
        a (int, float): number one
        b (int, float): number two

    Returns:
        (int, float): sum of two number
    """
    return a + b


def minus(a, b):
    """ to subtract two number

    Args:
        a (int, float): number one
        b (int, float): number two

    Returns:
        (int, float): decrease of two number
    """
    return a - b


def multi(a, b):
    """to multiply two number

    Args:
        a (int, float): number one
        b (int, float): number two

    Returns:
        (int, float): multiply of two number
    """
    return a * b


def div(a, b):

    """to divide two number

    Args:
        a (int, float): number one
        b (int, float): number two

    Returns:
        (int, float): to divide of two number
    """
    if b == 0:
        return "Division by zero is not allowed."

    return a / b


def calculator():
    """Addition, subtraction, multiplication, 
    and division operations are performed. 
    First, the two numbers entered are performed, 
    and then the sign is entered.
    """
    try:
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter second number: "))
    except: 
        print("Pleas Enter Only numbers")
        return
    sign = input("Enter sign: ")

    if sign == '+':
        print(add(num_1, num_2))

    elif sign == '-':
        print(minus(num_1, num_2))

    elif sign == '*':
        print(multi(num_1, num_2))

    elif sign == '/':
        print(div(num_1, num_2))

if __name__ == 'main':
    calculator()





