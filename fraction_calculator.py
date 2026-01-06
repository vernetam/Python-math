'''
 Fraction operations
 '''
from fractions import Fraction

def add(a, b):
    print('Result of addition: {}'.format(a+b))
def subtract(a,b):
    print('Result of subtraction: {}'.format(a-b))
def divide(a,b):
    try:
        print('Result of division: {}'.format(a/b))
    except ZeroDivisionError:
        print('Invalid. Division by zero detected')
def multiply(a,b):
    print('Result of multiplication: {}'.format(a*b))

if __name__ == '__main__':
    a = Fraction(input('Enter first fraction: '))
    b = Fraction(input('Enter second fraction: '))
    op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
    if op == 'Add': 
        add(a,b) 
    elif op == 'Subtract': 
        subtract(a,b) 
    elif op == 'Divide': 
        divide(a,b) 
    elif op == 'Multiply': 
        multiply(a,b)
    else:
        print('You didn\'t enter a valid operation. Please try again')