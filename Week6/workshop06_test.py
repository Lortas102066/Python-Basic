#These values can be changed
FIT1045 = True
SHOW_ALL_INFO = False



#############################################################################

#Import statements
from workshop06 import *
import workshop06
from math import ceil
from contextlib import redirect_stdout
import io
from collections.abc import Iterable

def fail_output(s):
    print("{}".format("="*60))
    print(s)
    print("{}".format("="*60))

def communicate(func, input, ans):
    print("checking: {}({})=={}".format(func, input, ans))

def get_function(module, method):
    return getattr(module, method, None)

def get_output(function, func_input, marking=False):
    try:
        f = io.StringIO()
        with redirect_stdout(f):
            #for when there is more than 1 arg
            if isinstance(func_input, tuple):
                output = function(*func_input)
            else:
                output = function(func_input)
            return (False, output)
    except Exception as e:
        if not marking:
            print(e)
            fail_output(f"...fail (exception thrown)")
        return (True, None)

def process_output(output, ans, options):
    output_function, in_place = options
    if output_function and output:
        return (output_function(output) == output_function(ans))
    if in_place:
        returned_val, modified_var, answer = ans
        return (returned_val == output and modified_var == answer)

def run_cases(module, function, cases, processing, marking=False):
    verbose=SHOW_ALL_INFO
    if marking == True: verbose = False
    # Setup cases count
    cases_failed = 0
    # Run tests
    for case in cases:
        func, input, ans = case
        if verbose: communicate(func, input, ans)
        throws_error, output = get_output(function, input, marking)
        if throws_error:
            cases_failed += 1
            continue
        if output == ans: #or f.getvalue() == ans (used for printing values - no longer used)
            if verbose: print("...passed")
        else:
            if processing and process_output(output, ans, processing):
                if verbose: print("...passed after processing output")
            else:
                if not marking:
                    fail_output(f"...fail (incorrect output)\ngiven output:\t{output} \ncorrect output:\t{case[2]}")
                cases_failed += 1
    return (len(cases)-cases_failed) #num passed tests

def evaluate_module(module, tests, mod_mark=2.5, marking=False):
    if not marking:
        print(f"Evaluating module: {module.__name__}")
    res = 0
    max = 0 #max mark
    t_passed = 0 #percentage of tests passed
    total_tests = 0
    f_passed = 0 #number of functions with 0 errors
    for test in tests:
        cases, mark, *processing = test
        total_tests += len(cases)
        func = cases[0][0]
        if not marking:
            print("{}".format("#"*60))
            print()
            print(f"Testing function {func}:")
        max = max + mark
        # Get function that cases are tested on
        function = get_function(module, func)
        if not function:
            if not marking: print("...fail (function not found)")
            continue
        cases_passed = run_cases(module, function, cases, processing, marking=marking)
        total_cases = len(cases)
        res += round((cases_passed/total_cases)*mark, 4) #scale res by number of marks the function is worth
        t_passed += cases_passed
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

    if res/max>=0.95 and f_passed > 1: scaled = 2.5
    elif res/max>=0.7 and f_passed > 1: scaled = 2
    elif res/max>=0.5 and f_passed > 1: scaled = 1.5
    elif f_passed >= 1: scaled = 1
    elif res/max>0: scaled = 0.5
    if not marking:
        print(f"Percentage of tests passed: {round(t_passed/total_tests*100,2)}%")
        print(f"Scaled percentage of tests passed: {round(res/max*100,2)}%")
        print(f"Total correct functions: {f_passed}/{len(tests)}")
        print()
        print(f"Total marks: {scaled}/{mod_mark}")
    return scaled

#############################################################################

#Task 1
lst1 = [5] #0,0
lst1A = [5]
lst2 = [1,2,3] #0,2
lst2A = [3,2,1]
lst3 = [1,2,3,4,5,6,7] #3,3
lst3A = [1,2,3,4,5,6,7]
lst4 = [1,2,3,4,5,6,7] #2,5
lst4A = [1,2,6,4,5,3,7]

min_list = [5,2,3,10,1,10,5,6,5,8,10]

lst6 = [5]
lst6A = [5]
lst7 = [5,2,3,10,1,10,5,6,5,8,10]
lst7A = [1,2,3,5,5,5,6,8,10,10,10]
lst8 = [2,3,5,4]
lst8A = [2,3,4,5]
lst9 = [5,2,9,2]
lst9A = [2,2,5,9]

SWAP = \
  [('swap', (lst1,0,0), (None,lst1,lst1A)),
   ('swap', (lst2,0,2), (None,lst2,lst2A)),
   ('swap', (lst3,3,3), (None,lst3,lst3A)),
   ('swap', (lst4,2,5), (None,lst4,lst4A))]

FIND_MIN = \
  [('find_min', ([5],0), 0),
   ('find_min', (min_list,0), 4),
   ('find_min', (min_list,5), 6),
   ('find_min', (min_list,8), 8)]

SELECTION = \
  [('selection_sort', lst6, (None,lst6,lst6A)),
   ('selection_sort', lst7, (None,lst7,lst7A)),
   ('selection_sort', lst8, (None,lst8,lst8A)),
   ('selection_sort', lst9, (None,lst9,lst9A))]

#Task 2
lst10 = [5] #0
lst10A = [5]
lst11 = [1,2,3] #2
lst11A = [1,2,3]
lst12 = [2,3,4,1,5,6,7] #3
lst12A = [2,3,1,4,5,6,7]
lst13 = [1,2,4,5,6,7,3] #6
lst13A = [1,2,4,5,6,3,7]

lst14 = [5] #0
lst14A = [5]
lst15 = [1,2,3] #2
lst15A = [1,2,3]
lst16 = [2,3,4,1,5,6,7] #3
lst16A = [1,2,3,4,5,6,7]
lst17 = [1,2,4,5,6,7,3] #6
lst17A = [1,2,3,4,5,6,7]

lst18 = [5]
lst18A = [5]
lst19 = [5,2,3,10,1,10,5,6,5,8,10]
lst19A = [1,2,3,5,5,5,6,8,10,10,10]
lst20 = [2,3,5,4]
lst20A = [2,3,4,5]
lst21 = [5,2,9,2]
lst21A = [2,2,5,9]

SWAP_DOWN = \
  [('swap_down', (lst10,0), (None,lst10,lst10A)),
   ('swap_down', (lst11,2), (None,lst11,lst11A)),
   ('swap_down', (lst12,3), (None,lst12,lst12A)),
   ('swap_down', (lst13,6), (None,lst13,lst13A))]

SHUFFLE = \
  [('shuffle_down', (lst14,0), (None,lst14,lst14A)),
   ('shuffle_down', (lst15,2), (None,lst15,lst15A)),
   ('shuffle_down', (lst16,3), (None,lst16,lst16A)),
   ('shuffle_down', (lst17,6), (None,lst17,lst17A))]

INSERTION = \
  [('insertion_sort', lst18, (None,lst18,lst18A)),
   ('insertion_sort', lst19, (None,lst19,lst19A)),
   ('insertion_sort', lst20, (None,lst20,lst20A)),
   ('insertion_sort', lst21, (None,lst21,lst21A))]


#Task 3
empty_m = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]

simple_m = [[0,1,1,1],
            [1,0,1,0],
            [1,1,0,0],
            [1,0,0,0]]

example_m = [[0,1,1,1,0],
             [1,0,0,0,0],
             [1,0,0,1,1],
             [1,0,1,0,1],
             [0,0,1,1,0]]

DEGREE = \
  [('degree', (empty_m, 0), 0),
   ('degree', (simple_m, 1), 2),
   ('degree', (example_m, 2), 3)]

SHARED = \
  [('shared_friends', (empty_m,0,1), []),
   ('shared_friends', (simple_m,1,2), [0]),
   ('shared_friends', (example_m,0,4), [2,3])]

ARE_FRIENDS = \
  [('are_friends', (empty_m,0,1), False),
   ('are_friends', (simple_m,1,2), True),
   ('are_friends', (example_m,0,4), False)]

CLIQUE = \
  [('clique', (empty_m,[0,1]), False),
   ('clique', (simple_m,[0,1,2],), True),
   ('clique', (example_m,[2,3,4]), True)]

evaluate = \
  [(SWAP, 0.25, None, True),
   (FIND_MIN, 0.25),
   (SELECTION, 0.5, None, True),
   (SWAP_DOWN, 0.25, None, True),
   (SHUFFLE, 0.25, None, True),
   (INSERTION, 0.5, None, True),
   (DEGREE, 0.5),
   (SHARED, 0.5, sorted, False),
   (ARE_FRIENDS, 0.5),
   (CLIQUE, 0.5)] 

#evaluate += [] if FIT1045 else [(task5, 2, output_process)] #weight is 2 for adv
################################################################################

def main():
    if details() == ('', '@student.monash.edu', ''):
        print("Tester will not run if details are not completed.")
        return
    evaluate_module(workshop06, evaluate, marking=False)


def mark():            
    num,email,name = details()
    score = evaluate_module(workshop06, evaluate, marking=True)
    print(','.join([num,email,name,str(score)]))

if __name__ == "__main__":
    main()
