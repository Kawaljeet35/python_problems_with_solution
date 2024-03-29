"""
Happy Number

Write a program in python to check if a given number
is a Happy number or not.
The program should return a boolean.
"""

#Solution:
def isHappy(number):
    if number == 1:
        return True
    else:
        seen = set()
        while number != 1 and number not in seen:
            seen.add(number) 
            sum_of_squares = 0
            for char in str(number): 
                digit = int(char)
                sum_of_squares += digit ** 2
            number = sum_of_squares 
        return number == 1

print(isHappy(13))
