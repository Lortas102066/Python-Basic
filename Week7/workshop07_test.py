#These values can be changed
FIT1045 = True
SHOW_ALL_INFO = False

#############################################################################

#Import statements
from workshop07 import *
import workshop07
from math import ceil
from contextlib import redirect_stdout
import io
from collections.abc import Iterable
# Extra Import Statements for test cases
from math import log, isclose, sin, pi


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
    if len(options) == 2:
        output_function, in_place = options
    else:
        output_function, in_place = options, False

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

#Task 1A - Merge
lst1a = []
lst1b = ['f']
lst1c = ['f']

lst2a = [1, 3, 7, 8, 11]
lst2b = [-3, -1, 1, 3, 9]
lst2c = [-3, -1, 1, 1, 3, 3, 7, 8, 9, 11]

lst3a = [1, 2, 3]
lst3b = [4, 5, 6, 7]
lst3c = [1, 2, 3, 4, 5, 6, 7]

lst4a = ['a', 'b', 'c']
lst4b = []
lst4c = ['a', 'b', 'c']


MERGE = \
    [('merge', (lst1a, lst1b), lst1c),
     ('merge', (lst2a, lst2b), lst2c),
     ('merge', (lst3a, lst3b), lst3c),
     ('merge', (lst4a, lst4b), lst4c)]



#Task 1B Merge Sort
lst5 = [3, 7, 9, 6, 2, 5, 4, 1, 8]
lst5a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst6 = [11, 0, 1, 5, 7, 2]
lst6a = [0, 1, 2, 5, 7, 11]
lst7 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
lst7a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


MERGESORT = \
    [('merge_sort', (lst5), lst5a),
     ('merge_sort', (lst6), lst6a),
     ('merge_sort', (lst7), lst7a)]


#Task 1C
# No test cases for this task but weighting is 0.5, will be marked manually
ANALYSIS_SORT = \
    [('stubbed', (), ())]


# Task 2
# This Part of this task will be marked manually
points = [(350, 150), (500, 250), (150, 150), (50, 400), (200,100)]

OFF_TO_MERGE = \
    [('offices_to_merge', points, (2,4))]


#Task 3 EXTENSION - FIT1053
# Test Cases will be in the doctest of the original workshop file
REG_FALSI = \
    [('root', (), ())] # This case is a stub

evaluate = \
  [(MERGE, 0.25, None),
   (MERGESORT, 0.25, None),
   (ANALYSIS_SORT, 0.5, None),
   (OFF_TO_MERGE, 1, None)]
   #(#task, #weight, #output process)] #weight should add to 1 per tasks

evaluate += [] if FIT1045 else [(REG_FALSI, 1, None)] #weight is 2 for adv 
# Note: This week's tester will give FIT1045 students a maximum mark of 2/2.5 and 1.5/2.5 for 1053 students.
################################################################################

def main():
    if details() == ('', '@student.monash.edu', ''):
        print("Tester will not run if details are not completed.")
        return
    evaluate_module(workshop07, evaluate, marking=False)


def mark():            
    num,email,name = details()
    score = evaluate_module(workshop07, evaluate, marking=True)
    print(','.join([num,email,name,str(score)]))

if __name__ == "__main__":
    main()
