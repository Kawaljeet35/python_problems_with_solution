"""
Armstrong Number

Write a program in python to check if a given number
is an Amstrong number or not.
The program should return a boolean.
"""

#Solution:
def isArmstrongNumber(number):
    number = str(number)
    n = len(number)
    sum = 0
    for i in range(0,n):
        sum += int(number[i]) ** n
    return sum == int(number)
        
print(isArmstrongNumber(2))
