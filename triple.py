def tripler(function):
    '''
    Wrap the function that the function is used on three times

    Parameter
    ---------
    function:
            function for getting value used on three times
    Return
    ------
    inner fucntion
            Calls the actual function(wrapper)
    '''
    def wrapper():
        '''
        Calculate the time for the function
        '''
        for i in range(3):
            function()
    return wrapper

def bye():
    '''
    the value used on three times.
    '''
    print("Bye")

result = tripler(bye)
result()