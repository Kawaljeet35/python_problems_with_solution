"""
Factorial

Write a function in python which takes an integer as an input
and return its factorial.

Example Input/Output:
print(factorial(1))   Output: 1
print(factorial(2))   Output: 2
print(factorial(3))   Output: 6
print(factorial(4))   Output: 24
print(factorial(5))   Output: 120
"""

#Solution:
def factorial(n):
    if n <=2:
        return n
    else:
        return n*factorial(n-1)
    
print(factorial(6)) #Try experimenting with different values
