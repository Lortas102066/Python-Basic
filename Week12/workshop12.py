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

#Back Tracking
    def solutions(completed, options, partial=[]):
        if completed(partial):
            return [partial]
        else:
            res = []
            for o in options(partial):
                augmented = partial+[o]
                res += solutions(completed, options, augmented)
        return res

# Part A - Palindromic Bitlists (0.5 Marks)
def palindrome_binary(n):
    """
    Input: integer n
    Output: list of bitlists in lexicographical order where each bitlist is
            a palindrome.
    
    For Example:
    >>> palindrome_binary(2)
    [[0, 0], [1, 1]]
    >>> palindrome_binary(3)
    [[0, 0, 0], [0, 1, 0], [1, 0, 1], [1, 1, 1]]
    >>> palindrome_binary(4)
    [[0, 0, 0, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 1, 1, 1]]
    """
    pass
    def completed(partial):
        return len(partial) == n

    def options(partial):
        if len(partial) < n//2 + n%2 :
            return [0,1]
        return [partial[n-len(partial)-1]]

    return solutions(completed, options)


# Part B - All Paths (0.5 Marks)
def all_paths(M, u, v):
    """
    Input: Graph 'M' as adjacency matrix, and vertexes 'u' and 'v'
    Output: List of vertices in lexicographical order that finds 
            all paths from 'u' to 'v'.
    
    For Example:
    >>> M = [ [0, 1, 1, 0],
    ...       [1, 0, 1, 1],
    ...       [1, 1, 0, 0],
    ...       [0, 1, 0, 0]]
    >>> all_paths(M, 0, 1)
    [[0, 1], [0, 2, 1]]
    >>> all_paths(M, 1, 0)
    [[1, 0], [1, 2, 0]]
    >>> all_paths(M, 0, 3)
    [[0, 1, 3], [0, 2, 1, 3]]
    >>> all_paths(M, 2, 3)
    [[2, 0, 1, 3], [2, 1, 3]]
    """
    pass
    def completed(partial):
            return partial[-1] == v

    def options(partial):
        last = partial[-1]
        return [i for i in range(len(M)) if M[last][i] == 1 and i not in partial]

    return solutions(completed, options, [u])

# Part C - Stairs (0.5 Marks)
def stairs(staircase):
    """
    Input: Bitlist (list of lists) representing a staircase input where 1
           represents a safe stair, and 0 represents an unsafe stair.
    Output: An integer which represents the number of possible ways to
            climb the stairs given the restrictions by allowing to jump
            the staircase by jumping one step, two steps or three steps; but
            you are not allowed to jump the same number of steps twice in a
            row.
    
    For Example:
    >>> stairs([1, 1, 0, 1, 1])
    3
    >>> stairs([1, 0, 1, 0, 1])
    0
    >>> stairs([1, 0, 0, 1])
    1
    >>> stairs([1, 1, 0, 1])
    2
    >>> stairs([1, 1, 1, 1])
    3
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)