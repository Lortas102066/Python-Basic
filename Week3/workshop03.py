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
def partial_sum(start, end, step):
    """
    >>> partial_sum(3, 13, 2)
    48
    >>> partial_sum(8, 290, 5)
    8436
    >>> partial_sum(-5, 30, 3)
    138
    >>> partial_sum(-10, -100, -5)
    -1045
    """
    pass

    current_val = start
    answer = 0
    while current_val <= end:
        answer = answer + current_val
        current_val += step
    return answer
        

###Task 2
def reverse_strings(my_list):
    """
    >>> reverse_strings([])
    ''
    >>> reverse_strings(['my','little','pony'])
    'ponylittlemy'
    >>> reverse_strings(['00','11','22','33'])
    '33221100'
    """
    pass
    reverse_index = -1
    answer2 = ''
    for i in range(len(my_list)):
        answer += my_list[reverse_index]
        reverse_index += -1
    return answer2

def complete(my_list):
    """
    >>> complete([12, 15, 19])
    [12, 13, 14, 15, 16, 17, 18, 19]
    >>> complete([2, 3])
    [2, 3]
    >>> complete([1])
    [1]
    >>> complete([-5, 0, 5])
    [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    """
    pass
    first_num = my_list[0]
    last_num = my_list[-1]
    loop_val = 0
    current_num = 0
    answer2B= []
    while current_num < last_num:
        current_num = first_num + loop_val
        answer3.append(current_num)
        loop_val += 1
    return answer2B
    

###Task 3
def addition_table(numbers):
    """
    >>> addition_table([2, 5, -3, 7])
    [[3, 6, -2, 8], [4, 7, -1, 9], [5, 8, 0, 10]]
    >>> addition_table([1])
    [[2], [3], [4]]
    >>> addition_table([-2, -5, -9, -12, -23])
    [[-1, -4, -8, -11, -22], [0, -3, -7, -10, -21], [1, -2, -6, -9, -20]]
    """
    pass
    add_nums = [1, 2, 3]
    answer3 = []
    for i in add_nums:
        row = [num + i for num in numbers]
        answer3.append(row)
    return answer3

###Task 4
def remove_outliers(table):
    """
    >>> remove_outliers([[0, 4], [2, 4], [-1, 3]])
    [[0, 1.5], [2, 1.5], [1.5, 3]]
    """
    pass
    max_val = max(max(sublist) for sublist in table)  
    min_val = min(min(sublist) for sublist in table)  
    average = (max_val + min_val) / 2  
    for i in range(len(table)):
        for j in range(len(table[i])):
            if max_val == table[i][j]:
                table[i][j] = average
            elif min_val == table[i][j]:
                table[i][j] = average
    return table


###Task 5 - Extension (OPTIONAL)
def primes_in_range(start, stop):
    """
    >>> primes_in_range(35, 100)
    [37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    >>> primes_in_range(211, 263)
    [211, 223, 227, 229, 233, 239, 241, 251, 257, 263]
    >>> primes_in_range(35400, 35500)
    [35401, 35407, 35419, 35423, 35437, 35447, 35449, 35461, 35491]
    >>> primes_in_range(51854787, 51854830)
    [51854801, 51854807, 51854809, 51854821, 51854827]
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
