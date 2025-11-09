'''
 Unit converter: Miles and Kilometers
 '''
def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')

    print('3. Kilograms to Pounds')
    print('4. Pounds to Kilograms')

    print('5. Celcius to Farenheit')
    print('6. Farenheit to Celcius')

def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609
    print('Distance in miles: {0}'.format(miles))
def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609
    print('Distance in kilometers: {0}'.format(km))

def kg_lbs():
    kg = float(input('Enter mass in kilograms: '))
    lbs = kg * 2.205
    print('Mass in pounds: {}'.format(lbs))
def lbs_kg():
    lbs = float(input('Enter mass in pounds: '))
    kg = lbs / 2.205
    print('Mass in kilograms: {}'.format(kg))

def c_f():
    c = float(input('Enter temperature in celsius: '))
    f = 9/5 * 35 + 32
    print('Temperature in farenheit: {}'.format(f))
def f_c():
    f = float(input('Enter temperature in farenheit: '))
    c = 5/9 - (f - 32)
    print('Temperature in celsius: {}'.format(c))

if __name__ == '__main__':
    print_menu() 
    choice = input('Which conversion would you like to do?: ') 
    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()
    if choice == '3':
        kg_lbs()
    if choice == '4':
        lbs_kg()
    if choice == '5':
        c_f()
    if choice == '6':
        f_c()