# -*- coding: utf-8 -*-
"""
This script shows how to access the previous element in a list comprehension 
"""

from itertools import accumulate


def FibonacciRecursiveFunction(n: int) -> list:
    """
    Ilustration on how to use recursive lambda function
    to generate fibonacci series.
    """
    fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)
    return [fib(i) for i in range(n)]

# def ExampleItertoolsFuntion(n: int) -> list:
#     """
#     Ilustration on how to use itertools.

#     Documentation: https://docs.python.org/3/library/itertools
#     Itertools E.g. 
#     list(accumulate([1,2,3,4,5], lambda prev, element: prev + element))
    
#     Reduce E.g.
#     reduce(lambda x, n: [x[1], x[0]+x[1]], range(n), [0, 1])[0]
#     """
#     curr = 0
#     return list(accumulate(range(1,n), lambda prev, elem: prev * elem))


def ExampleAssignmentExpressions(n: int) -> list:
    """
    Ilustration on how to use assignment expressions
    to generate a fibonacci series.

    Documentation: https://peps.python.org/pep-0572/
    Assignment Expressions  -> Python version: >= 3.8
    E.g. [y := f(x), y**2, y**3]
    """
    i0,i1 = -1, 1 
    return [i1 := i0 + (i0 := i1) for j in range(n)]



if __name__ == '__main__':
    n=8
    print(
        FibonacciRecursiveFunction(n),
        # ExampleItertoolsFuntion(n),
        ExampleAssignmentExpressions(n),
        sep='\n'
    )
    