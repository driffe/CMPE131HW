def parse_input():
    '''
    Get user input

    This function is simply getting user input and then, split it with " ".

    Return
    ------
    list
        The list of splited user input

    Examples
    ------
    >>> 1 + 2 
    ['1', '+', '2']
    >>> 2 ** 3.5
    ['2', '**', '3.5']
    '''
    fullEq = input("Enter equation: ")
    eq = fullEq.split(" ")
    number1 = eq[0]
    number2 = eq[2]
    operator = eq[1]

    answer = calculator(number1, number2, operator)
    print(answer)

def add(number1, number2):
    '''
    Add up two numbers

    This function is equivalent to operator "+"

    Parameters
    ----------
    number1: float
        First number to add
    number2: float
        Second number to add
    
    Returns
    -------
    float
        The sum of "number1" and "number2"
    
    Examples
    >>> add(1.2, 3)
    4.2
    >>>add(4, 5)
    9.0
    '''
    return number1 + number2

def substract(number1, number2):
    '''
    Substract two numbers

    This function is equivalent to operator "-"

    Parameters
    ----------
    number1: float
        First number to substract
    number2: float
        Second number to substract
    
    Returns
    -------
    float
        The substraction of "number1" and "number2"
    
    Examples
    >>> substract(3, 2)
    1.0
    >>>substract(10, 4.9)
    5.1
    '''
    return number1 - number2

def multiply(number1, number2):
    '''
    Multiply two numbers

    This function is equivalent to operator "*"

    Parameters
    ----------
    number1: float
        First number to multiply
    number2: float
        Second number to multiply
    
    Returns
    -------
    float
        The multiplication of "number1" and "number2"
    
    Examples
    >>> multiply(1, 3)
    3.0
    >>>multiply(2, 3.4)
    6.8
    '''
    return number1 * number2

def divide(number1, number2):
    '''
    Divide two numbers

    This function is equivalent to operator "/"

    Parameters
    ----------
    number1: float
        First number to divide
    number2: float
        Second number to divide
    
    Returns
    -------
    float
        The division of "number1" and "number2"
    
    Examples
    >>> divide(3, 2)
    1.5
    >>>divide(10, 3.3)
    3.0303030303030303
    '''
    return number1 / number2 

def intDivide(number1, number2):
    '''
    Divide two numbers

    This function is equivalent to operator "//"

    Parameters
    ----------
    number1: float
        First number for floor division
    number2: float
        Second number for floor division
    
    Returns
    -------
    float
        The integer division of "number1" and "number2"
    
    Examples
    >>> divide(3, 2)
    1.0
    >>>divide(10, 3.3)
    3.0
    '''
    return number1 // number2

def power(number1, number2):
    '''
    number1 power of number2

    This function is equivalent to operator "**"

    Parameters
    ----------
    number1: float
        First number is base
    number2: float
        Second number is exponent
    
    Returns
    -------
    float
        number1^ number2
    
    Examples
    >>> power(3, 2)
    9.0
    >>>divide(10, 3)
    1000.0
    '''
    return number1 ** number2

def calculator(number1, number2, operator):
    '''
    Calculate the equation

    The function detect input from user. Only return result when input is valid. If not, return False.

    Parameters
    ----------
    number1: float
        First number for calculation
    number2: float
        Second number for calculation
    operator: str
        Operator for calculation

    Returns
    -------
    float
        result for calculation of equation
    
    Examples
    --------
    >>>calculator(2, 1, +)
    3.0
    >>>calculator(2, 4.1, *)
    8.2

    '''
    result = 0
    #check that input(number1, number2) is float for valid equation.
    try:
        number1 = float(number1)
        number2 = float(number2)
    except ValueError:
        return False
    #check which operator have to use. 
    if operator ==  "+":
        result = add(number1, number2)
    elif operator == "-":
        result = substract(number1, number2)
    elif operator == "*":
        result = multiply(number1, number2)
    elif operator == "/":
        result = divide(number1, number2)
    elif operator == "//":
        result = intDivide(number1, number2)
    elif operator == "**":
        result = power(number1, number2)
    else:
        return False
    return result

parse_input()