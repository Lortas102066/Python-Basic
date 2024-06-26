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

def is_in(char, string):
    """
    Input: a string char of a single character (you may limit to alphanumeric), and a string string comprising
    both upper and lower case alphanumeric and non-alphanumeric characters.
    1Output: a boolean, True if char is found in string; otherwise False.
    """
    index_pointer = 0
    while index_pointer < len(string):
        if char == string[index_pointer]:
            return True
        index_pointer += 1
    return False

def is_sorted(seq):
    """
    Input: a sequence seq of comparable elements.
    Output: a boolean, True if for all items in the list, the item at index i is less than or equal to the item at
    index i + 1; otherwise False.
    """
    for i in range(len(seq)-1):
        if seq[i] > seq[i+1]:
            return False
    return True

def abs(x): 
    if x >= 0:
        return x
    else:
        return 0-x

def max(lst):
    """
    Input: a non-empty sequence (list) of comparable objects lst.
    Output: the largest item in lst.
    """
    temp = lst[0]
    for i in range (len(lst)):
        if temp < lst[i]:
            temp = lst[i]
    return temp

def min(lst):
    """
    Input: a non-empty sequence (list) of comparable objects lst.
    Output: the smallest item in lst.
    """
    temp = lst[0]
    for i in range (len(lst)):
        if temp > lst[i]:
            temp = lst[i]
    return temp
        

def sum(lst):
    """
    Input: a sequence (list) of numbers lst.
    Output: the sum of all numbers in lst.
    """
    total_num = 0
    for i in range(len(lst)):
        total_num += lst[i]
    return total_num



def enumerate(seq, start = 0):
    """
    Input: a sequence seq, and an optional argument, an integer start. The default parameter value for start
    is 0.
    Output: a list of tuples, where each tuple is of the form (n, element). If start=0, n will be the index of
    the element, otherwise n will be the index of the element, offset by start.
    """
    enum = []
    for i in range(len(seq)):
        enum.append((i + start, seq[i]))
    return enum

def filter(function, seq):
    """
    Input: a function function and a sequence seq.
    Output: a list of elements from seq that when used as input in function return a value that is evaluated
    to True using Python’s standard truth testing procedure. The relative order between elements must be
    maintained.
    """
    filtered_items = []
    for item in seq:
        if function(item):
            filtered_items.append(item)
    return filtered_items
