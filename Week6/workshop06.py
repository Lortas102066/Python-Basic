from sys import float_info
from math import pi

# Student details
def details():
    student_number = '33554714' #write your student number as a string
    student_email = 'mmor0077' + '@student.monash.edu' #write your student email
    name = 'Mitsuki Morinaga' #write your name as it appears on Moodle
    return str(student_number), student_email, name


# Task 1
def swap(lst, a, b):
    """
    >>> family = ['Ransom', 'Linda', 'Walt', 'Joni']
    >>> swap(family, 3, 2)
    >>> family
    ['Ransom', 'Linda', 'Joni', 'Walt']
    """
    pass
    lst[a], lst[b] = lst[b], lst[a]


def find_min(lst, index):
    """
    >>> find_min(['candlestick', 'pipe', 'rope', 'knife', 'wrench'], 2)
    3
    >>> find_min([1, 3, 5, 11, 7, 3, 2, 6, 2], 3)
    6
    """
    pass
    min_val = lst[index]
    for i in lst[index:]:
        if i < min_val:
            min_val = i
    return lst.index(min_val)
    


# Selection sort
def selection_sort(lst):
    """
    >>> outsiders = ['Marta', 'Edi', 'Frank', 'Benoit']
    >>> selection_sort(outsiders)
    >>> outsiders
    ['Benoit', 'Edi', 'Frank', 'Marta']
    """
    pass
    for i in range(len(lst)-1):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]

        

# Task 2
def swap_down(lst, j):
    """
    >>> shawshank = ['Andy', 'Red', 'Tommy', 'Brooks']
    >>> swap_down(shawshank, 2)
    >>> shawshank
    ['Andy', 'Red', 'Tommy', 'Brooks']
    >>> swap_down(shawshank, 3)
    >>> shawshank
    ['Andy', 'Red', 'Brooks', 'Tommy']
    """
    pass
    if lst[j] < lst[j-1]:
        lst[j], lst[j-1] = lst[j-1], lst[j]


def shuffle_down(lst, k):
    """
    >>> club = ['Ben', 'Eddie', 'Bill', 'Richie', 'Stanley', 'Beverly', 'Mike']
    >>> shuffle_down(club, 5)
    >>> club
    ['Ben', 'Beverly', 'Eddie', 'Bill', 'Richie', 'Stanley', 'Mike']
    """
    pass
    while k > 0 and lst[k] < lst[k-1]:
            temp = lst[k]
            lst[k] = lst[k-1]
            lst[k-1] = temp
            k -= 1


def insertion_sort(lst):
    """
    >>> hawkins = ['Mike', 'Eleven', 'Dustin', 'Lucas', 'Will']
    >>> insertion_sort(hawkins)
    >>> hawkins
    ['Dustin', 'Eleven', 'Lucas', 'Mike', 'Will']
    """
    pass
    length = len(lst)
    for i in range(1, length):
        insert = i - 1
        val = lst[i]
        while insert >= 0 and lst[insert] > val:
            lst[insert + 1] = lst[insert]
            insert -= 1
        lst[insert + 1] = val
    pass


# Task 3
def degree(graph, v):
    """
    >>> friends = [[0, 1, 1, 1, 0],
    ...            [1, 0, 0, 0, 0],
    ...            [1, 0, 0, 1, 1],
    ...            [1, 0, 1, 0, 1],
    ...            [0, 0, 1, 1, 0]]
    >>> degree(friends, 0)
    3
    >>> degree(friends, 1)
    1
    >>> degree(friends, 4)
    2
    """
    pass
    count = 0
    for i in range(len(graph)):
        if graph[v][i] == 1:
            count += 1
    return count




def shared_friends(graph, u, v):
    """
    >>> friends = [[0, 1, 1, 1, 0],
    ...            [1, 0, 0, 0, 0],
    ...            [1, 0, 0, 1, 1],
    ...            [1, 0, 1, 0, 1],
    ...            [0, 0, 1, 1, 0]]
    >>> shared_friends(friends, 0, 4)
    [2, 3]
    """
    pass
    common_friends = []
    for i in range(len(graph)):
        if graph[u][i] == 1 and graph[v][i] == 1:
            common_friends.append(i)
    return common_friends


def are_friends(graph, u, v):
    """
    >>> friends = [[0, 1, 1, 1, 0],
    ...            [1, 0, 0, 0, 0],
    ...            [1, 0, 0, 1, 1],
    ...            [1, 0, 1, 0, 1],
    ...            [0, 0, 1, 1, 0]]
    >>> are_friends(friends, 0, 4)
    False
    >>> are_friends(friends, 0, 1)
    True
    """
    pass
    if graph[u][v] == 1 and graph[v][u] == 1:
        return True
    else:
        return False


def clique(graph, vertices):
    """
    >>> friends = [[0, 1, 1, 1, 0],
    ...            [1, 0, 0, 0, 0],
    ...            [1, 0, 0, 1, 1],
    ...            [1, 0, 1, 0, 1],
    ...            [0, 0, 1, 1, 0]]
    >>> clique(friends, [2, 3, 4])
    True
    >>> clique(friends, [0, 1, 2])
    False
    """
    pass
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            if not are_friends(graph, vertices[i], vertices[j]):
                return False
    return True


# Task 4 (Extension: Not Assessed)
def root(f, a, b, acc=float_info.min):
    """
    Input : continuous function f, floats a, b, and acc
            such that the signs of f(a) and f(b) differ
    Output: float x such that abs(f(x))<=acc

    For example:
    >>> from math import log, isclose
    >>> isclose(root(log, 0.1, 2), 1.0)
    True
    >>> def p(x): return 1-x**2
    >>> isclose(root(p, -2, 0), -1.0)
    True
    >>> isclose(root(p, 0, 100), 1.0)
    True
    >>> from math import sin, pi, isclose
    >>> isclose(root(sin, 1, 4), pi)
    True
    """
    pass


if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)