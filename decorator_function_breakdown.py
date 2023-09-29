"""
Here’s a short example that shows how decorator functions work under the hood. If it helps you understand decorators better, this script has succeeded.

Take these two functions, that can be used in tandem. The idea is that the first function, pname(), changes the behaviour of the second function, myfunc(), but without changing that function. This is the goal of decorator functions in Python.
"""


def p_name(func):
    def wrap():
        print("1")
        func()
        print("2")
    return wrap


def myfunc():
    print("34")


"""
When run solely, myfunc() prints “34”. When used in combination with p_name, we will output 3 strings: “1”, “34” and “2”. How to do this?

There are two options without using the “@” syntax that is used for decorators. This third option is covered last. These examples are meant to illustrate what the “@” syntax does. Also, it shows you don’t have to use that syntax to get the same results.

Option 1: using two statements
Using two statements, we can get the required results, which is printing three different strings. First, create a new variable and assign it to p_name(myfunc). This variable now refers to the inner function of p_name, but without running it. This is probably the most confusing part of decorator functions, but the only thing is does is pass function 2 to function 1 as an argument without running it. This means it stores a function reference, not its output.

In other words, the variable “myf” is an object referencing the p_name function with the second function as its argument. Next, call that variable as it is a function that will return whatever wrap() returns: 3 different strings. Mission accomplished.
"""
myf = p_name(myfunc)

myf()

"""
prints 
1
34
2
"""

"""
Option 2: using a single statement
The second option is a single statement that combines the previous two statements in a single one, namely calling p_name(myfunc) directly, without assinging it as a variable and adding a single pair of brackets, so that we call the myfunc() function explicitly as a function parameter of the p_name function. This is possible as functions are objects and can be passed as such to other functions. This is done as follows and produces the exact same output as the first option:
"""


def p_name(func):
    def wrap():
        print("1")
        func()
        print("2")
    return wrap


def myfunc():
    print("34")


p_name(myfunc)()

""" 
output:
1
34
2
"""
"""
This last snippet can be rewritten using the “@” syntax as follows and produces the same output as before:
"""
# The same code, now using @


def p_name(func):
    def wrap():
        print("1")
        func()
        print("2")
    return wrap


@p_name
def myfunc():
    print("34")


myfunc()

"""
output:
1
34
2
"""
