# Name: Mitsuki Morinaga        Student ID: 33554714


x = 3
y = 5
# Task 1: Maths
# Replace the '' in each line with one of [+, -, *, //, %, /, **]
# to create a statement that evaluates to True. 
# For example, (a) can be changed to:
0 == (x + x) % x

# We start by assigning values to variables x and y


# a
print(0 == (x - x) * x )
# b
print(4 == x * (y + x) % y )
# c
print(7.5 == (x * y) / (y - x))

# Task 2: Booleans
# Replace the '' in each line with one of [==, !=, <=, >=, <, >]
# to create a statement that evaluates to True.
# For example, (a) can be changed to:
10 <= 10

#a
print(10 == 10)
#b
print(10%4 != 12//7)
#c
print(3**2 != 10-3)

# Task 3: Temperature Conversion
# Replace the '' with a numerical expression that converts the
# temperature in Fahrenheit (temp_f) to the temperature in Celsius.
# For instance, if Celsius were 3 degrees more than Fahrenheit (incorrect!),
# the implementation would be:
# temp_c = temp_f + 3

temp_c = 0
temp_f = 70
temp_c = (temp_f-32) * 5/9

# Task 4: Name Factoids
# Replace the '' with an expression that evaluates to a string with
# the following pattern:
# factoids = '<name> has <number of letters>. It starts with <letter> and ends with <letter>.'
# For example, if you do not change the given name, factoids would
# evaluate to:
#     'Jane has 4 letters. It starts with J and ends with e.'
# NOTE: You must implement factoids so that it would work for any value
#       assigned to name.

name = 'Mitsuki'
factoids = len(name)
first = name[0]
last = name[-1]
print(name + " has " + str(factoids) + " characters. It starts with " + first + " and ends with " + last + ".")


# Task 5: Coin Flip (Extension task)
# THIS TASK IS OPTIONAL

# Replace the '' with any necessary import statements
''
import random
bias = random.randint(0, 100)
flip_coin = random.randint(0, 1)
user_input = int(input('What is your guess? (0 or 1)'))
def flip():
    print("The bias for true is " + str(bias) + ".")
    print("Your guess is " + str(user_input))
    if flip_coin == user_input:
        print("You guess it right!" + " The answer is " + str(flip_coin))
    else:
        print('You miss the guess! The answer is ' + str(flip_coin))
    
    return None

flip()