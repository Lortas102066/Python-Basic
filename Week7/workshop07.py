from math import sqrt, pi
from sys import float_info
import random # For task1c
import timeit # For task1c
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


# Task 1A - Merge
def merge(lst1, lst2):
    """
    Input: Two sorted lists lst1, lst2
    Output: One sorted list 'res' merged together
    >>> merge([1, 2, 4, 6], [3, 5, 7, 8])
    [1, 2, 3, 4, 5, 6, 7, 8]

    >>> merge([1, 2, 3], [4, 5, 6])
    [1, 2, 3, 4, 5, 6]

    >>> merge([11, 13, 15], [])
    [11, 13, 15]

    >>> merge([], [16, 18, 20])
    [16, 18, 20]
    """
    pass
    merged = []
    i = 0
    j = 0
    
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    
    while i < len(lst1):
        merged.append(lst1[i])
        i += 1
    
    while j < len(lst2):
        merged.append(lst2[j])
        j += 1
    
    return merged


# Task 1B - Merge Sort
def merge_sort(lst):
    """
    Input: list of elements
    Output: Sorted list of elements
    >>> merge_sort([3, 7, 9, 6, 2, 5, 4, 1, 8])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> merge_sort([11, 0, 1, 5, 7, 2])
    [0, 1, 2, 5, 7, 11]

    >>> merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    pass
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def InsertionSort(aList):
    length = len(aList)
    for k in range(1, length):
        temp = aList[k]
        insert = k - 1
        while insert >= 0 and aList[insert] > temp:
            aList[insert+1] = aList[insert]
            insert -= 1
        aList[insert+1] = temp
    
def selectionSort(aList):
    for index in range(len(aList)-1):
        minPos = index 
        for current in range(index+1, len(aList)): # Find minimum index
            if aList[current] < aList[minPos]:
                minPos = current
        aList[minPos], aList[index] = aList[index], aList[minPos] # Swap

# Task 1C - Analysis of Sorting Algorithms
import timeit
import random
def sort_analysis(func, n):
    """
    Input: The sort function as an argument and 'n' which represents the
           no. of elements of the input lists you will create.
    Output: A dictionary of the sorting order (i.e., keys) and times (i.e., values)
            for the specific sort.

    ANALYSIS: <WRITE YOUR PARAGRAPH HERE>
    """
    pass





# Task 2 - Post Offices
import math
def dist(p1, p2):
    """Computes Eucledian distance between points p1 and p2.
    """
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return distance


def offices_to_merge(points):
    """
    Input : list of 2d coordinates of post offices,
            points=[(x1, y1), (x2, y2)...(xn, yn)]} with n>1
    Output: a pair of indices (l, k) such that...
            for all pairs of indices 0 <= i < j <=n it holds that
            dist(points[l], points[k]) <= dist(points[i], points[j])
    
    For example:
    >>> points = [(350, 150), (500, 250), (150, 150), (50, 400), (200,100)]
    >>> offices_to_merge(points)
    (2, 4)
    """
    min_distance = float('inf') # max distance. Reference(https://www.geeksforgeeks.org/python-infinity/)
    min_indices = (0, 0)
    
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = dist(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                min_indices = (i, j)
    
    return min_indices
            


# Task 3 - Regula Falsi: Extension (OPTIONAL)
def sign(x):
    pass
    
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


# Task 1C - Analysis of Sorting Algorithms
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
