"""
Prime Checker

Write a program that determines whether the input number is a prime number or not.
The input number will be a positive integer.

Exapmple outputs: 
17 is a prime number.
23 is a prime number.
27 is not a prime number.
"""


#Solution:
def primeCheck(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break  
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

n = int(input("Check this number: "))
primeCheck(n)
