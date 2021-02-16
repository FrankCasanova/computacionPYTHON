import doctest
def factorial (n):
    '''
    -calcula el factorial de n-

    >>> factorial(4)
    24

    '''
    # print(n)
    if n == 1:
        return 1
    return n * factorial(n-1)    

n = int(input('escribe un entero: '))


doctest.testmod()

print(factorial(n))