from doctest import testmod
#test function: 
def squareOfNum(n):
    """"
    This function returns the square of any given number
    >>> squareOfNum(5)
    25
    >>> squareOfNum(10)
    100
    >>> squareOfNum(8)
    88
    """
    return n*n

# def testFunc(x):
#     """"
#     This function is to test the testing.
#     >>> if x%2 ==0:
#     ...    return 'Even'
#     ... else:
#     ...    'Odd'
#     Even 
#     Even 
#     Odd
#     """
#     print("Even")
#     print("Even")
#     print("Odd")
#     if x+2%2 == 0:
#         return 'Even'
#     else:
#         return 'Odd'
    

if __name__ == '__main__':
    print("Using function: ",squareOfNum(99))
    testmod()
    # testmod(name = 'squareOfNum', verbose=False) #Shows only failure

