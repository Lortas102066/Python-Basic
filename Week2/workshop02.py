from random import random
'''
DO NOT CHANGE THE NAME OF THIS FILE, or else the tester will not work. 
The first function requires that you replace the given strings with
your personal details. It is important that you enter your student number
and your student email correctly. If your number and email do not match we
will then check your name, so your name acts as a failsafe.
'''
# Student details
def details():
    student_number = '33554714' #write your student number as a string
    student_email = 'mmor0077' + '@student.monash.edu' #write your student email
    name = 'Mitsuki Morinaga' #write your name as it appears on Moodle
    return str(student_number), student_email, name

###Task 1
def calculate(x,y,operator):
    if operator == '+':
        result = x + y
        print(result)
    elif operator == '-':
        result = x - y
        print(result)
    elif operator == '/':
        result = x / y
        print(result)
    elif operator == '%':
        result = x % y
        print(result)
    elif operator == '*':
        result = x * y
        print(result)

calculate(3, 5, '+')

###Task 2
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 100 == 0):
        return True
        if year < 2021:
            print('Year' + year + ' was a leap year')
        else: 
            print('Year' + year + ' will be a leap year')
    else:
        return False
        if year > 2021:
            print('Year' + year + ' was not a leap year')
        else: 
            print('Year' + year + ' will not be a leap year')
    """
    >>> is_leap_year(1)
    False
    >>> is_leap_year(100)
    False
    >>> is_leap_year(2000)
    True
    >>> is_leap_year(2019)
    False
    >>> is_leap_year(2040)
    True
    >>> is_leap_year(2100)
    False
    """
    pass

def leap_year_answer(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 100 == 0):
        return True
        if year < 2021:
            print('Year' + year + ' was a leap year')
        else: 
            print('Year' + year + ' will be a leap year')
    else:
        return False
        if year < 2021:
            print('Year' + year + ' was not a leap year')
        else: 
            print('Year' + year + ' will not be a leap year')
    """
    >>> leap_year_answer(1)
    'Year 1 was not a leap year'
    >>> leap_year_answer(100)
    'Year 100 was not a leap year'
    >>> leap_year_answer(2000)
    'Year 2000 was a leap year'
    >>> leap_year_answer(2019)
    'Year 2019 was not a leap year'
    >>> leap_year_answer(2040)
    'Year 2040 will be a leap year'
    >>> leap_year_answer(2100)
    'Year 2100 will not be a leap year'
    """
    pass

###Task 3
def next_triangular_number(num):
    total_num = 0
    adding_number = 1
    while num >= total_num:
            total_num = total_num + adding_number
            adding_number = adding_number + 1
    print(int(total_num))
            
next_triangular_number(3)
            
"""
    >>> next_triangular_number(5)
    6
    >>> next_triangular_number(25)
    28
    >>> next_triangular_number(40)
    45
    >>> next_triangular_number(2000)
    2016
    """
pass

###Task 4
def add(numbers):
    addition_of_second_number = 0
    for i in range(1, len(numbers)):
        if i % 2 == 1:
            addition_of_second_number += numbers[i]
        else:
            print('use a valid number')
    print(addition_of_second_number)
        
"""
    >>> add([])
    0
    >>> add([25])
    0
    >>> add([92, 61, 97, 10, -39])
    71
    >>> add([-24, -25, -33, 32, -81, -58, 28, -4, -30, -69, 44, -41])
    -165
    """
pass

bin = '101000'
flip_num = ''
def flip(binary_string):

    for i in range(len(bin)):
        if bin[i] == '0':
            flip_num += '1'
        elif bin[i] == '1':
            flip_num += '0'
    print(flip_num)
    """
    >>> flip('')
    ''
    >>> flip('01')
    '10'
    >>> flip('101')
    '010'
    >>> flip('001011111111')
    '110100000000'
    """
    pass

###Task 5 - Extension (OPTIONAL)
def n_even_fibonacci(n):
    first_num = 0
    second_num = 1
    answer = 0
    even_counter = 0

    while even_counter < n:
        first_num = second_num
        second_num = answer
        answer = first_num + second_num
        if answer % 2 == 0:
            print(answer)
            even_counter += 1
        else:
            0
    """
    >>> n_even_fibonacci(0)
    []
    >>> n_even_fibonacci(5)
    [0, 2, 8, 34, 144]
    >>> n_even_fibonacci(10)
    [0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418]
    >>> n_even_fibonacci(12)
    [0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578]
    """
    pass


###Challenge - OPTIONAL
from math import e
def estimate_e(error):
    """
    <WRITE YOUR ANALYSIS HERE>
    >>> estimate_e(1)
    2.0
    >>> estimate_e(0.1)
    2.6666666666666665
    >>> estimate_e(0.01)
    2.708333333333333
    >>> estimate_e(0.005)
    2.7166666666666663
    >>> estimate_e(0.001)
    2.7180555555555554
    >>> estimate_e(0.0000000001)
    2.7182818284467594
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
