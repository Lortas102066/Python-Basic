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


# Task 1
def convert_temp(temps):
    """
    Input: Given a list of temperatures in fahrenheit.
    Output: A list of values converted all to celsius.

    >>> convert_temp([90.0, 50.9, 84.6, 100.3])
    [32.22222222222222, 10.499999999999998, 29.222222222222218, 37.94444444444444]
    """
    pass
    temprature_in_celsius = [(temp - 32) / 1.8 for temp in temps]
    return temprature_in_celsius


def square_odds(lst):
    """
    Input: A sequence of numbers.
    Output: A list with all of the odd numbers squared.

    >>> square_odds([1, 2, 3, 4, 5, 6, 7])
    [1, 9, 25, 49]
    """
    pass
    odd_list = [item**2 for item in lst if item % 2 != 0]
    return odd_list
    

def only_numbers(in_str):
    """
    Input: A string that has letters and numbers.
    Output: A list numbers with all the letters removed
            and numbers converted to integers.

    >>> only_numbers('abcdef12345')
    [1, 2, 3, 4, 5]
    >>> only_numbers('c4t,d0g,b14d,fI5h')
    [4, 0, 1, 4, 5]
    """
    pass
    numbers = [int(item) for item in in_str if item.isnumeric()]
    return numbers


def fizz_buzz(num): # Not Assessed (Optional)
    """
    Input: An integer (num) that represents the total number in list.
    Output: A list that from 0 to num (inclusive) that 
            if the current number is divisible by 3, the element 
            should say "FIZZ", if divisible by 5, the number should 
            say BUZZ, if divisible by both 3 and 5 should say FIZZBUZZ, 
            if neither the element append the number.
    
    >>> fizz_buzz(5)
    [0, 1, 2, 'FIZZ', 4, 'BUZZ']
    >>> fizz_buzz(15)
    [0, 1, 2, 'FIZZ', 4, 'BUZZ', 'FIZZ', 7, 8, 'FIZZ', 'BUZZ', 11, 'FIZZ', 13, 14, 'FIZZBUZZ']
    """
    pass



# Task 2 - Warmup
def common_bf(a, b):
    pass
    common_list = []
    for item_a in a:
        for item_b in b:
            if item_a == item_b:
                common_list.append(item_a)

def common(a, b):
    """ Computes list of elements common to a and b.

    Input : two lists, a and b, each without duplicate
            elements
    Output: list of all elements x such that
            x in a and x in b

    For example:
    >>> common([5, 46, -25, 3], [2, -1, 10])
    []
    >>> c = common([8, 5, 27, -2, 10], [-3, 5, -27, 10])
    >>> set(c) == {5, 10}
    True
    """
    pass
    a = sorted(a)
    b = sorted(b)
    common_list = []
    pointer_a = 0
    pointer_b = 0
    while pointer_a < len(a) and pointer_b < len(b):
        if a[pointer_a] == b[pointer_b]:
            common_list.append(a[pointer_a])
            pointer_a += 1
            pointer_b += 1
        elif a[pointer_a] < b[pointer_b]:
            pointer_a += 1
        else:
            pointer_b += 1
    return common_list


# Task 3
def pairs_of_sum(lst, s):
    """ Finds pairs of list elements with specific sum.

    Input : list of unique integers (lst),
            integer (s)
    Output: list containing all pairs (x, y) of elements 
            of lst such that x < y and x + y = s

    For example:
    >>> pairs_of_sum([7, 1, 25, 10], 5)
    []
    >>> pairs_of_sum([7, 1, 25, 10], 32)
    [(7, 25)]
    >>> pairs = pairs_of_sum([-2, 4, 0, 11, 7, 13], 11)
    >>> set(pairs) == {(0, 11), (4, 7), (-2, 13)}
    True
    """
    pass
    lst = sorted(lst)
    pairs_list = []
    pointer_a = 0
    pointer_b = len(lst) - 1
    while pointer_a < pointer_b:
        if lst[pointer_a] + lst[pointer_b] == s:
            pairs_list.append((lst[pointer_a], lst[pointer_b]))
            pointer_a += 1
            pointer_b -= 1
        elif lst[pointer_a] + lst[pointer_b] < s:
            pointer_a += 1
        else:
            pointer_b -= 1
    return pairs_list

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)