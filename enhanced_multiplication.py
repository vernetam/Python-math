'''
Multiplication table printer
'''
def multi_table(a,b):
    for i in range(1, b+1):
        print('{0} x {1} = {2}'.format(a, i, a*i))
        
if __name__ == '__main__':
    try:
        a = int(input("Please enter an integer you wish to multiply: "))
        b = int(input("Up to which multiple would you like to multiply to: "))
        multi_table(a,b)
    except ValueError:
        print("Incorrect value. Ensure input is an integer.")