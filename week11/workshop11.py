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


# Warmup
def lex_less_eq(a, b):
    """Determines whether sequence (a) is lexicographically less or equal to
    sequence (b); equivalent to a <= b.

    For example:
    >>> lex_less_eq('tactic', 'tree')
    True
    >>> lex_less_eq('tactic', 'tactical display')
    True
    >>> lex_less_eq([1, 2, 3], [0, 1, 2, 3])
    False
    """
    pass
    for i in range(min(len(a), len(b))):
        if a[i] < b[i]:
            return True
        elif a[i] > b[i]:
            return False
    return len(a) <= len(b)


# Task 1: Part A - Recursive Bitlist
def rbitlists(n):
    """Generates list of all bitlists of length n in lexicographic order
    using recursion.

    For example.
    >>> rbitlists(2)
    [[0, 0], [0, 1], [1, 0], [1, 1]]
    >>> rbitlists(3)
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]

    <Write your explanation here>
    """
    pass
    if n == 0:
        return [[]]
    else:
        new_list = rbitlists(n - 1)
        
        return [[0] + i for i in new_list] + [[1] + j for j in new_list]


# Task 1: Part B - Recursive Permutations
def rpermutations(lst):
    """ Generates all permutations of input list.
    
    >>> sorted(rpermutations(list(range(1, 4))))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(rpermutations(list(range(1, 5))))
    [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]
    >>> sorted(rpermutations(list('JOE')))
    [['E', 'J', 'O'], ['E', 'O', 'J'], ['J', 'E', 'O'], ['J', 'O', 'E'], ['O', 'E', 'J'], ['O', 'J', 'E']]

    <Write your explanation here>
    """
    pass
    if len(lst) == 0:
        return [[]]
    else:
        permutations = []
        
        for i in range(len(lst)):
            rest = lst[:i] + lst[i+1:]
            for p in rpermutations(rest):
                permutations.append([lst[i]] + p)
                
        return permutations

# Task 2: Part B1 - Bounded Lists
def bounded_lists(upper_bounds):
    """
    Input: List of positive integers of length 'n'
    Output: List of lists where i, lst[i] <= upper_bound[i]

    >>> bounded_lists([1, 1, 2])
    [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]]
    """
    pass
    if not upper_bounds:
        return [[]]
    
    else:
        answer = []
        
        for list in bounded_lists(upper_bounds[:-1]):
            for i in range(upper_bounds[-1] + 1):
                answer.append(list + [i])
        return answer


# Task 2: Part 1 - Greedy Exchange
def greedy_exchange(amount, denominations):
    """
    >>> greedy_exchange(56, [20, 10, 5, 1])
    [2, 1, 1, 1]
    >>> greedy_exchange(350, [100, 50, 10, 5, 2, 1])
    [3, 1, 0, 0, 0, 0]
    >>> greedy_exchange(12, [9, 6, 5, 1])
    [1, 0, 0, 3]
    """
    pass
    exchange = [0] * len(denominations)
    for i, money in enumerate(denominations):        #enumerate finds the index and the item of the list reference: 
        while amount >= money:
            amount -= money
            exchange[i] += 1
    return exchange

    
# Task 2: Part B2 - Brute Force Implementation
def brute_force_coin_exchange(amount, denominations):
    """
    Input: The target amount of you want to reach and a list of 
           coins (i.e. denominations) that you have an infinite amount of.
    Output: A list of integers where each index represents the number of 
            coins the denominations list.

    >>> brute_force_coin_exchange(15, [10, 7, 6, 1])
    [0, 2, 0, 1]
    """
    pass
    upper_bounds = [amount // coin for coin in denominations]
    all_combinations = bounded_lists(upper_bounds)

    combination = []
    for combo in all_combinations:
        total = 0
        for i in range(len(denominations)):
            total += denominations[i] * combo[i]
        if total == amount:
            combination.append(combo)

    optimal_solution = None
    min_coin_count = float('inf')
    
    for i in combination:
        coin_count = 0
        for j in i:
            coin_count += j
        if coin_count < min_coin_count:
            min_coin_count = coin_count
            optimal_solution = i

    return optimal_solution if optimal_solution != None else [0] * len(denominations)


# Task 2: Part C - Backtracking Implementation
def backtracking_exchange(amount, denominations):
    """
    >>> backtracking_exchange(56, [20, 10, 5, 1])
    [2, 1, 1, 1]
    >>> backtracking_exchange(12, [9, 6, 5, 1])
    [0, 2, 0, 0]
    """
    pass


if __name__=='__main__':
    import doctest
    doctest.testmod()