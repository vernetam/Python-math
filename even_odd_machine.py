def print_machine(x):
    i = 0
    j = x
    while i < 9:
        print(j + 2)
        i += 1
        j += 2

if __name__ == "__main__":
    try:
        num = float(input("Please enter an integer value: "))
        if not num.is_integer():
            print("That is not an integer.")
        if num % 2 == 0:
            print("{0} is even".format(num))
        if num % 2 != 0:
            print("{0} is odd".format(num))
        print_machine(num)
    except ValueError:
        print("That is an invalid input.")

# Test comment