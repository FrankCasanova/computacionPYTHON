import doctest

def suma(num1,num2):
    '''
    -suma 2 números-
    
    >>> suma(2,2)
    4
    
    '''
    return num1 + num2


doctest.testmod()