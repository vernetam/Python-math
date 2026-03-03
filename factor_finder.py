from sympy import Symbol, factor, sympify, pprint
from sympy.core.sympify import SympifyError

if __name__ == "__main__":
    x = Symbol('x')
    y = Symbol('y')
    while True:
        try:
            exp = input('Enter the expression to be factored: ')
            exp_factored = factor(exp)
            pprint(exp_factored)
        except SympifyError:
            print('Invalid error. Please try again')
        end_program = input('Would you like to exit program? Enter y/Y to exit: ')
        if end_program == 'y' or end_program == 'Y':
            break
    
