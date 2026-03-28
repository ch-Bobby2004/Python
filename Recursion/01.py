'''Recursion in Python is a programming technique where a function calls itself to solve a problem by breaking it down into smaller, similar subproblems.

Basic Idea

A recursive function has two main parts:

Base case → stops the recursion
Recursive case → the function calls itself '''


def print_desc(n):
    if n == 0:   # Base case
        return
    print(n)
    print_desc(n - 1)

print_desc(5)



def print_asc(n):
    if n == 0:   # Base case
        return
    print_asc(n - 1)
    print(n)

print_asc(5)