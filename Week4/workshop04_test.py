#These values can be changed
FIT1045 = True
SHOW_ALL_INFO = False



#############################################################################

#Import statements
from workshop04 import *
import workshop04
from math import ceil
from contextlib import redirect_stdout
import io
from collections.abc import Iterable
from builtins import round as builtin_round

def fail_output(s):
    print("{}".format("="*60))
    print(s)
    print("{}".format("="*60))

def run_cases(module, cases, output_function=None, verbose=SHOW_ALL_INFO, marking=False):
    cases_failed = 0
    if marking == True: verbose = False
    for case in cases:
        if verbose:
            print("checking: {}({})=={}".format(case[0], case[1], case[2]))
        method = getattr(module, case[0], None)
        if not method:
            if not marking:
                print("...fail (method not found)")
            return 0,0 #Different for THIS WORKSHOP ONLY
        try:
            f = io.StringIO()
            with redirect_stdout(f):
                #for when there is more than 1 arg
                if isinstance(case[1], tuple):
                    output = method(*case[1])
                else:
                    output = method(case[1])
        except Exception as e:
            if not marking:
                print(e)
                fail_output(f"...fail (exception thrown)")
            cases_failed += 1
            continue
        if output == case[2] or f.getvalue() == case[2]:
            if verbose:
                print("...passed")
        else:
            if output_function and output_function(output) == output_function(case[2]):
                    if verbose and not marking:
                        print("...passed after processing output")
            else:
                if not marking:
                    fail_output(f"...fail (incorrect output)\ngiven output:\t{output} \ncorrect output:\t{case[2]}")
                cases_failed += 1
    return (len(cases)-cases_failed, len(cases))

def evaluate_module(module, tests, mark=2.5, marking=False):
    if not marking:
        print(f"Evaluating module: {module.__name__}")
    res = 0
    max = 0 #max mark
    t_passed = 0 #percentage of tests passed
    total_tests = 0
    f_passed = 0 #number of functions with 0 errors
    for test in tests:
        if not marking:
            print("{}".format("#"*60))
            print()
            print(f"Testing function {test[0][0][0]}:")
        cases_passed, total_cases = run_cases(module, test[0], test[2], marking=marking)
        #Different for THIS WORKSHOP ONLY
        if total_cases==0: continue
        max = max + test[1]
        ####
        res += builtin_round((cases_passed/total_cases)*test[1],4) #scale res by marks function is worth
        t_passed += cases_passed
        total_tests += total_cases
        if cases_passed==total_cases: f_passed += 1
        if not marking:
            if cases_passed==total_cases:
                print("All cases passed")
            else:
                print("Some cases failed")
            print()
    if not marking:
        print("{}".format("#"*60))
        print()

    #Scale and print Results
    scaled = 0

    if max==0: return 0 #Different for THIS WORKSHOP ONLY
    
    if res/max>=0.95 and f_passed > 1: scaled = 2.5
    elif res/max>=0.7 and f_passed > 1: scaled = 2
    elif res/max>=0.5 and f_passed > 1: scaled = 1.5
    elif f_passed >= 1: scaled = 1
    elif res/max>0: scaled = 0.5
    if not marking:
        print(f"Percentage of tests passed: {builtin_round(t_passed/total_tests*100,2)}%")
        print(f"Scaled percentage of tests passed: {builtin_round(res/max*100,2)}%")
        print(f"Total correct functions: {f_passed}/{len(tests)}")
        print()
        #print(f"Total marks: {scaled}/{mark}")
    return f_passed #different return statement

#############################################################################

#Simple Functions
IS_IN = \
  [('is_in', ('a', ''), False),
   ('is_in', ('a', 'abc'), True),
   ('is_in', ('a', 'cba'), True),
   ('is_in', ('a', 'ABC'), False)]

IS_SORTED = \
  [('is_sorted', ([]), True), #list
   ('is_sorted', ([-3, 0, 2, 2, 4]), True),
   ('is_sorted', ([4, 2, 2, 0, -3]), False), 
   ('is_sorted', ([1, 3, 2, 2, 4]), False),
   ('is_sorted', (""), True), #string
   ('is_sorted', ("aabcd"), True),
   ('is_sorted', ("dcbaa"), False),
   ('is_sorted', ("acbde"), False)]

ABS = \
    [('abs', (0), 0),
     ('abs', (5), 5),
     ('abs', (-5), 5),
     ('abs', (2.75), 2.75),
     ('abs', (-2.75), 2.75)]

ALL = \
    [('all', ([]), True),
     ('all', ([True, True, True, True]), True),
     ('all', ([True, True, True, False]), False),
     ('all', ([1, -4, "cat", [[]]]), True),
     ('all', ([1, -4, "cat", []]), False)]

ANY = \
    [('any', ([]), False),
     ('any', ([False, False, True, False]), True),
     ('any', ([False, False, False, False]), False),
     ('any', ([None, 0, "", -1]), True),
     ('any', ([None, 0.0, "", ()]), False)]

MAX = \
    [('max', ([10, 4, 6, 2, 1]), 10),
     ('max', ([1, 4, 6, 2, 10]), 10),
     ('max', ([-11, -40, -60, -20, -10]), -10),
     ('max', ([-10, -40, -60, -20, -11]), -10),
     ('max', (['c', 'a', 't']), 't'),
     ('max', (['A', 'a', 'a']), 'a')]

MIN = \
    [('min', ([10, 4, 6, 2, 1]), 1),
     ('min', ([1, 4, 6, 2, 10]), 1),
     ('min', ([-101, -40, -60, -20, -10]), -101),
     ('min', ([-10, -40, -60, -20, -11]), -60),
     ('min', (['c', 'a', 't']), 'a'),
     ('min', (['A', 'a', 'a']), 'A')]

rev_seq = [1, 2, 3, 4, 5]
rev_seq_reversed = [5, 4, 3, 2, 1]
REVERSED = \
    [('reversed', ([]), []), #list
     ('reversed', ([1, 2, 3]), [3, 2, 1]),
     ('reversed', ([3.5, 'a', (4, 7)]), [(4,7),'a', 3.5]),
     ('reversed', (""), ""), #string
     ('reversed', ("cats are cool"), ['l','o','o','c',' ',
          'e','r','a',' ','s','t','a','c']),
#NATHAN
     ('reversed', rev_seq, rev_seq_reversed), #check original seq untouched
     ('reversed', rev_seq, rev_seq_reversed)] 

SUM = \
    [('sum', ([]), 0),
     ('sum', ([1, 2, 3, 4]), 10),
     ('sum', ([-1, -2, -3, -4]), -10),
     ('sum', ([1, -2, 3, -4]), -2)]

#COMPLEX FUNCTIONS
BIN = \
    [('bin', (0), '0b0'),
     ('bin', (5), '0b101'),
     ('bin', (-5), '-0b101'),
     ('bin', (8314), '0b10000001111010')]

ENUMERATE = \
    [('enumerate', ([]), []),
     ('enumerate', ([0,1,2]), [(0,0),(1,1),(2,2)]),
     ('enumerate', (['cat', 'dog', 'horse'], 5), [(5,'cat'),(6,'dog'),(7,'horse')]),
     ('enumerate', ('cat dog'),
          [(0,'c'),(1,'a'),(2,'t'),(3,' '),(4,'d'),(5,'o'),(6,'g')])]

def filter_a(x):
    return x == 2
def filter_b(x):
    return x[0] == "b"

FILTER = \
    [('filter', (filter_a, []), []),
     ('filter', (filter_a, [2, 2, 4, 5, 2]), [2, 2, 2]),
     ('filter', (filter_b, ['bat', 'cat', 'able', 'match', 'bear']),
          ['bat', 'bear'])]

def map_a(x):
    return x*2
def map_b(x):
    return x + " Bennet"

MAP = [
    ('map', (map_a, []), []),
    ('map', (map_a, [0, 5, 2]), [0, 10, 4]),
    ('map', (map_a, ['a', 'b', 'c']), ['aa','bb','cc']),
    ('map', (map_b, ['Lizzie', 'Jane', 'Lydia']), ["Lizzie Bennet", "Jane Bennet", "Lydia Bennet"])]

LIM_RANGE = \
    [('lim_range', (5,5), []), #start, stop
     ('lim_range', (0,5), [0,1,2,3,4]),
     ('lim_range', (0,0,21), []), #start, stop, step
     ('lim_range', (5, 0, -1), [5,4,3,2,1]),
     ('lim_range', (-1, -5, -1), [-1,-2,-3,-4]),
     ('lim_range', (0, 6, 2), [0,2,4]),
     ('lim_range', (0, 5, 10), [0])]

ROUND = \
    [('round', (0.22), 0),
     ('round', (-0.22), 0),
     ('round', (0.5), 0),
     ('round', (5.844, 1), 5.8),
     ('round', (5.848, 2), 5.85),
     ('round', (3.55, 1), 3.6),
     ('round', (3.45, 1), 3.4)]

SET = \
    [('set', ([]), []),
     ('set', ([0,8,4,4,6,5,9,4]), [4,0,5,6,8,9]),
     ('set', ([4, 4, -4, 4, 4, 4]), [-4,4])]

SORTED = \
    [('sorted', ([]), []),
     ('sorted', ([4,3,2,1]), [1,2,3,4]),
     ('sorted', ([-1, 0, 6, -3]), [-3, -1, 0, 6]),
     ('sorted', ('second'), ['c', 'd', 'e', 'n', 'o', 's']),
     ('sorted', ('first'), ['f','i','r','s','t'])]

SIMPLE_FUNCTIONS = \
    [(IS_IN, 1, None),
     (IS_SORTED, 1, None),
     (ABS, 1, None),
     (ALL, 1, None),
     (ANY, 1, None),
     (MAX, 1, None),
     (MIN, 1, None),
     (REVERSED, 1, None),
     (SUM, 1, None)]

COMPLEX_FUNCTIONS = \
    [(BIN, 1, None),
     (ENUMERATE, 1, None),
     (FILTER, 1, None),
     (MAP, 1, None),
     (LIM_RANGE, 1, None),
     (ROUND, 1, None),
     (SET, 1, sorted),
     (SORTED, 1, None)]

NUM_COMP = (2 if FIT1045 else 4)
TOTAL = 8

################################################################################

def combined_score(simple, comp):
    if comp >= NUM_COMP and simple+comp >= TOTAL:
        return 2.5
    if comp >= NUM_COMP//2 and simple+comp >= TOTAL:
        return 2
    if comp>= NUM_COMP//2 or simple+comp >= 4:
        return 1.5
    if simple+comp >= 2:
        return 1
    if simple+comp >= 1:
        return 0.5
    return 0

def main():
    print('##Simple Functions:##')
    simp = evaluate_module(workshop04, SIMPLE_FUNCTIONS, marking=False)
    print('##Complex Functions:##')
    comp = evaluate_module(workshop04, COMPLEX_FUNCTIONS, marking=False)
    scaled = combined_score(simp, comp)
    #Print score
    print("{}".format("#"*60))
    print(f"Total marks: {scaled}/2.5")


def mark():            
    num,email,name = details()
    score = combined_score(
        evaluate_module(workshop04, SIMPLE_FUNCTIONS, marking=True),
        evaluate_module(workshop04, COMPLEX_FUNCTIONS, marking=True))
    print(','.join([num,email,name,str(score)]))

if __name__ == "__main__":
    main()
