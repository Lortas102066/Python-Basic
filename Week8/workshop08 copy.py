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


def gcd(a, b):
    """ Determines greatest common divisor of two integers.
    
    Input : two integers a and b such that not a==b==0
    Output: greatest common divisor of a and b
    
    For example:
    >>> gcd(0, 4)
    4
    >>> gcd(10, 0)
    10
    >>> gcd(18, 27)
    9
    >>> gcd(21, 13)
    1
    """
    pass
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def reverse(lst):
    """ Computes reverse of input sequence.
    
    Input : any list (lst)
    Output: reverse of lst
    
    For example:
    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reverse([10, 11, 12, 13, 14])
    [14, 13, 12, 11, 10]
    >>> reverse([1])
    [1]
    >>> reverse([])
    []
    """
    pass
    if len(lst) <= 1:
        return lst
    else:
        return reverse(lst[1:]) + [lst[0]] 


def is_pal(string):
    """Checks whether string is palindrome.
    
    Input : any string
    Output: True if string==string[::-1]
    
    For example:
    >>> is_pal('aa')
    True
    >>> is_pal('aabb')
    False
    >>> is_pal('aba')
    True
    """
    pass
    if len(string) <= 1:
        return True
    elif string[0] != string[-1]:
        return False
    else:
        return is_pal(string[1:-1])


from collections import deque
from graphs import neighbours, print_grid_traversal
import graphs
g = graphs.ex_tree

def bfs_traversal(graph, s, goals=[]):
    """
    >>> g = graphs.ex_tree
    >>> dfs_traversal(g, 0, {12})
    [0, 1, 2, 12]
    >>> print_grid_traversal(g, 10, bfs_traversal(g, 0, {12}))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---***---***---***---***---***---***   ***   
                 |                 |     |     |     |     |
    ***---***---***---***---***   ***   ***   ***   ***   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   ***---***   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    >>> print_grid_traversal(g, 10, bfs_traversal(g, 0, {22}))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---004---003---005---***---***---***---***---***   ***   
                 |                 |     |     |     |     |
    ***---***---006---***---***   ***   ***   ***   ***   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   ***---***   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    """
    pass
    visited = []
    boundary = [s]
    while len(boundary) > 0:
        v = boundary.pop(0)
        visited += [v]
        if v in goals:
            return visited
        for w in neighbours(v, graph):
            if w not in visited and w not in boundary:
                boundary.append(w)
    return visited



def dfs_traversal(graph, s, goals=[]):
    """
    >>> g = graphs.ex_tree
    >>> print_grid_traversal(g, 10, dfs_traversal(g, 0, {12}))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---***---***---***---***---***---***   ***   
                 |                 |     |     |     |     |
    ***---***---***---***---***   ***   ***   ***   ***   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   ***---***   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    >>> print_grid_traversal(g, 10, dfs_traversal(g, 0, {9, 40, 49}))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---***---***---***---***---***---***   ***   
                 |                 |     |     |     |     |
    ***---***---004---***---***   ***   ***   ***   ***   ***   
     |     |     |                       |           |      
    ***   ***   005---006---008---***   ***---***   ***---***   
     |     |           |     |                              
    ***   ***---***   007   009---010---011---012---013---014   
    """
    pass
    visited = []
    boundary = [s]
    while len(boundary) > 0:
        v = boundary.pop()
        visited += [v]
        if v in goals:
            return visited
        for w in neighbours(v, graph):
            if w not in visited and w not in boundary:
                boundary.append(w)
    return visited

def build_path(start, end, predecessors):
    route = [end]
    node = end
    while node != start:
        node = predecessors[node]
        route.insert(0, node)
    return route
def bfs_path(graph, s, goals=[]):
    """
    >>> g = graphs.ex_tree
    >>> print_grid_traversal(g, 10, bfs_path(g, 0, {22}))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---***---***---***---***---***---***   ***   
                 |                 |     |     |     |     |
    ***---***---004---***---***   ***   ***   ***   ***   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   ***---***   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    """
    pass
    queue = [s]
    seen = set()
    pred = [None] * len(graph)
    
    while queue:
        current = queue.pop(0)
        seen.add(current)
        if current in goals:
            return build_path(s, current, pred)
        for neighbour in neighbours(current, graph):
            if neighbour not in seen and neighbour not in queue:
                queue.append(neighbour)
                pred[neighbour] = current
    

def dfs_path(graph, s, goals=[]):
    """
    >>> g = graphs.ex_tree
    >>> print_grid_traversal(g, 10, dfs_path(g, 0, [9, 39]))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---004---005---006---007---008---009   ***   
                 |                 |     |     |     |     |
    ***---***---***---***---***   ***   ***   ***   010   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   011---012   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    """
    pass
    path_stack = [s]
    seen = set()
    ancestors = [None] * len(graph)

    while path_stack:
        node = path_stack.pop()
        seen.add(node)

        if node in goals:
            return build_path(s, node, ancestors)

        for neighbour in neighbours(node, graph):
            if neighbour not in seen and neighbour not in path_stack:
                path_stack.append(neighbour)
                ancestors[neighbour] = node

if __name__=='__main__':
    """
    <your paragraph with examples here>
    """

    import doctest
    doctest.testmod(verbose=True)
