# to set the value of the p2 attribute to 50 for the current instance of the class using a function, and then get the new value of p2, again using a function
class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)

p = ClassOne(1, 2)

setattr(p, 'p2', 50)
print(getattr(p, 'p2'))


# Considering the ClassOne class and the p object, write code on line 11 in order to check if p2 is an attribute of p, using a function, also printing the result to the screen.
class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)

p = ClassOne(1, 2)

print(hasattr(p, 'p2'))


# Considering the ClassOne class and the p object, write code on line 11 to check if p is indeed an instance of the ClassOne class, using a function, also printing the result to the screen.
class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)

p = ClassOne(1, 2)

print(isinstance(p, ClassOne))


# Considering the ClassOne class, write code starting on line 9 to create a child class called ClassTwo that inherits from ClassOne and also has its own method called times10() that takes a single parameter x and prints out the result of multiplying x by 10.
class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)

class ClassTwo(ClassOne):
    def times10(self, x):
        print(x * 10)


y = ClassTwo(10, 20)
print(y.p1)


# Considering the ClassOne and ClassTwo classes, where the latter is a child of the former, write code on line 15 in order to call the times10() method from the child class having x equal to 45, also printing the result to the screen.
class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)

class ClassTwo(ClassOne):
    def times10(self, x):
        return x * 10
        
obj = ClassTwo(15, 25)

print(obj.times10(45))


# Considering the ClassOne and ClassTwo classes, write code on line 13 to verify that ClassTwo is indeed a child of ClassOne, also printing the result to the screen.
class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)

class ClassTwo(ClassOne):
    def times10(self, x):
        return x * 10
        
print(issubclass(ClassTwo, ClassOne))


# Write a list comprehension on line 1 that will iterate over range(1, 5) and return a list of its elements.


