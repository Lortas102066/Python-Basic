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

# Warmup - (0.5 marks)
def is_upper_triangular(a):
    """
    Determines whether (a) is upper triangular.

    For example:
    >>> a = [[2, 1, 1],
    ...      [0, -8, -2],
    ...      [0, 0, 1]]
    >>> is_upper_triangular(a)
    True

    Input : square matrix (a)
    Output: True if all entries of (a) below diagonal are 0;
            False otherwise
    """
    pass
    dim = len(a)
    for row in range(dim):
        for col in range(row, dim):
            if a[row][col] == 0:
                return False
    return True

# Task 1 - Part A (0.5 marks)
def is_row_echelon(a):
    """Checks wether a is in echelon (staircase) form.

    >>> a = [[1, 1],
    ...      [0, 1]]
    >>> is_row_echelon(a)
    True

    >>> a = [[1, 0],
    ...      [1, 1]]
    >>> is_row_echelon(a)
    False

    >>> a = [[1, 0],
    ...      [0, 1]]
    >>> is_row_echelon(a)
    True

    >>> a = [[1, 1],
    ...      [0, 0]]
    >>> is_row_echelon(a)
    True

    >>> a = [[0, 0],
    ...      [0, 0]]
    >>> is_row_echelon(a)
    True

    >>> a = [[0, 0],
    ...      [0, 1]]
    >>> is_row_echelon(a)
    False

    >>> a = [[1, 1, 0, 1, 1],
    ...      [0, 0, 1, 0, 1],
    ...      [0, 0, 0, 0, 1],
    ...      [0, 0, 0, 0, 0],
    ...      [0, 0, 0, 0, 0]]
    >>> is_row_echelon(a)
    True
    """
    pass
    pivot_position_lst = []
    for row in range(len(a)):
        found_pivot = False
        for col in range(len(a[row])):
            if a[row][col] != 0:
                pivot_position_lst.append(col)
                found_pivot = True
                break
        if not found_pivot:
            pivot_position_lst.append(len(a))
            
    for i in range(1, len(pivot_position_lst)):
        if pivot_position_lst[i] < pivot_position_lst[i - 1]:
            return False
        elif pivot_position_lst[i] == pivot_position_lst[i - 1] and pivot_position_lst[i] != len(a):
                return False
    return True


# Task 1 - Part B (0.5 marks)
def pivot_index(a, j, p=None):
    """
    Finds pivot index of matrix a in column j.
    :param a: matrix with n columns
    :param j: column index less or equal n
    :return: row index k greater than j such that a[k][j]!=0 or None if no such index exists
    """
    pass
    if p is None:
        p = len(a)
    for row in range(j, p):
        if a[row][j] != 0:
            return row
    return None



def echelon(a, b):
    """
    Computes equivalent system in row echelon form of input system
    of linear equations by means of forward elimination. 

    >>> a = [[1, 1, 1],
    ...      [2, 0, 3],
    ...      [3, 1, 4]]
    >>> b = [2, 5, 6]
    >>> echelon(a, b)
    ([[1, 1, 1], [0.0, -2.0, 1.0], [0.0, 0.0, 0.0]], [2, 1.0, -1.0])
    
    >>> a = [[1, 1, 0, 1],
    ...      [-1, -1, 1, 0],
    ...      [-2, -2, -1, 1],
    ...      [-1, -1, -2, 1]]
    >>> b = [1, 0, 0, 0]
    >>> echelon(a, b)
    ([[1, 1, 0, 1], [0.0, 0.0, 1.0, 1.0], [0.0, 0.0, 0.0, 4.0], [0.0, 0.0, 0.0, 0.0]], [1, 1.0, 3.0, 0.0])
    """
    pass

# Task 1 - Part C (0.5 marks)
def solve_by_back_substitution(u, b):
    """
    Solves linear system ux=b for a square matrix u in row echelon
    form or returns None if no solution exists.

    >>> u = [[1, 1, 1],
    ...      [0, -2, 1],
    ...      [0, 0, 0]]
    >>> b = [2, 5, 6]
    >>> solve_by_back_substitution(u, b)

    >>> u = [[1, 1, 1],
    ...      [0, -2, 1],
    ...      [0, 0, 0]]
    >>> b = [2, 1, 0]
    >>> solve_by_back_substitution(u, b)
    [2.5, -0.5, 0.0]

    >>> u = [[1, 1, 0, 1, 1],
    ...      [0, 0, 1, 0, 1],
    ...      [0, 0, 0, 0, 1],
    ...      [0, 0, 0, 0, 0],
    ...      [0, 0, 0, 0, 0]]
    >>> b = [2, 2, 1, 0, 0]
    >>> solve_by_back_substitution(u, b)
    [1.0, 0.0, 1.0, 0.0, 1.0]
    """
    pass

# Task 2
# Warmup (0 marks)
def adjacency_matrix(adj_lists):
    """
    >>> lec_graph = [ [2, 4, 5, 6, 7],
    ...               [2, 3, 5, 6 ,7],
    ...               [0, 1, 6, 7],
    ...               [1, 4, 7],
    ...               [0, 3, 6],
    ...               [0, 1],
    ...               [0, 1, 2, 4, 7],
    ...               [0, 1, 2, 4, 7] ]
    >>> adjacency_matrix(lec_graph)
    [[0, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 1, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 0, 0, 1], [1, 1, 1, 0, 1, 0, 0, 1]]
    """
    pass
    n = len(adj_lists)
    matrix = [[0] * n for i in range(n)]

    for i in range(n):
        neighbors = adj_lists[i]
        for neighbor in neighbors:
            matrix[i][neighbor] = 1

    return matrix
    


# Part A: Independent Sets (0.5 marks)
def is_indset(adj_lists, a):
    """
    >>> lec_graph = [ [2, 4, 5, 6, 7],
    ...               [2, 3, 5, 6 ,7],
    ...               [0, 1, 6, 7],
    ...               [1, 4, 7],
    ...               [0, 3, 6],
    ...               [0, 1],
    ...               [0, 1, 2, 4, 7],
    ...               [0, 1, 2, 4, 7] ]
    >>> is_indset(lec_graph, [])
    True
    >>> is_indset(lec_graph, [5])
    True
    >>> is_indset(lec_graph, [0, 2])
    False
    >>> is_indset(lec_graph, [6, 5, 3])
    True
    """
    pass

# Part B - Greedy Maximisation (0.5 marks)
def greedy_indset(adj_lists):
    """
    <Describe the greedy strategy you used here>
    """
    pass


# Task 3 - Extension (OPTIONAL)
def polynomial_fit(points):
    """
    Input: list of co-ordinates (xi, yi) where all xi values are unique. 
    Output: list of the coefficients in order of associated power
    
    >>> points1 = [(1, 4), (-2, 1), (2, 13)]
    >>> polynomial_fit(points1)
    [-1.0, 3.0, 2.0]
	
    >>> points2 = [(-1, -9), (7, 15)]
    >>> polynomial_fit(points2)
    [-6.0, 3.0]
	
    >>> points3 = [(0, 0), (1, 27), (2, 0), (3, -33), (4, 0)]
    >>> polynomial_fit(points3)
    [0.0, 64.0, -40.0, 2.0, 1.0]
    """
    pass



if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)

