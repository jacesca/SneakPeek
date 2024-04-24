# Use the correct function from the itertools module on line 6, 
# in between the parentheses of list(), in order to concatenate list1 and list2.
import itertools

list1 = [1, 2, 3]
list2 = [4, 5]

result = list(itertools.chain(list1, list2))

print(result)


# join list of lists in python
import itertools
a = [['a','b'], ['c']]
print(list(itertools.chain.from_iterable(a)))


# Use the correct function from the itertools module with a for loop and a nested 
# if/else block in order to return all the numbers starting at 20 and up to 31 with a step of 2. 
# Be careful not to end up with an infinite loop!
import itertools

for i in itertools.count(start=20, step=2):
    if i < 31:
        print(i)
    else:
        break
        
        
# Use the correct function from the itertools module on line 5, in between the parentheses of list(), 
# in order to return the elements for which the lambda function given as an argument returns False.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>> # itertools.filterfalse(predicate, iterable)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>> # Make an iterator that filters elements from iterable returning only those for which the predicate is false. If predicate is None, return the items that are false. Roughly equivalent to:
# >>>>>>>>>>>>>>>>>>>>>>>>>>>> # Ex.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>> # def filterfalse(predicate, iterable):
# >>>>>>>>>>>>>>>>>>>>>>>>>>>> #     # filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
# >>>>>>>>>>>>>>>>>>>>>>>>>>>> #     if predicate is None:
# >>>>>>>>>>>>>>>>>>>>>>>>>>>> #         predicate = bool
# >>>>>>>>>>>>>>>>>>>>>>>>>>>> #     for x in iterable:
# >>>>>>>>>>>>>>>>>>>>>>>>>>>> #         if not predicate(x):
# >>>>>>>>>>>>>>>>>>>>>>>>>>>> #             yield x
import itertools

lam = lambda x: x < 5

result = list(itertools.filterfalse(lam, range(10)))

print(result)

