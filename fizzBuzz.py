"""
FizzBuzz Problem

Write a program that prints the numbers from 1 to 100. 
But for multiples of 3, print "Fizz" instead of the number, and for 
the multiples of 5, print "Buzz". 
For numbers which are multiples of both three and five, print "FizzBuzz".
Each number should be printed on a new line.

Example Output:
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
...
"""

#Solution:
for i in range(1,101):
    if(i%3 == 0 and i%5 == 0):
        print("FizzBuzz")
    elif(i%3 == 0):
        print("Fizz")
    elif(i%5 == 0):
        print("Buzz")
    else:
        print(i)
