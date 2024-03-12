"""
Password Generator

Write a Python program that generates secure passwords of varying lengths according 
to specified criteria. 
The program should prompt the user to input the desired password 
length within a range of 6 to 20 characters.
The password should be randomly generated and must contain 2 numbers, 2 symbols 
and both the lowercase and the uppercase alphabets.

Example Input/Output:

Enter desired password length: 12
Here is your password: pR@5sW8!qL2Z
"""


#solution:
import random

lower_alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                   "j", "k", "l", "m", "n", "o", "p", "q", "r",
                   "s", "t", "u", "v", "w", "x", "y", "z"]

upper_alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 
                   "J", "K", "L", "M", "N", "O", "P", "Q", "R", 
                   "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!","@","#","$","%","&","?","*"]

passLength = int(input("Enter desired password length: "))

passLengthGood = True
if passLength > 20 or passLength < 6:
    passLengthGood = False
    while not passLengthGood:
        print("Enter a password length between 6 and 20")
        passLength = int(input("Enter desired password length: "))  
        if 6 <= passLength <= 20:
            passLengthGood = True

password = []

for i in range(2):
    password.append(random.choice(numbers))

for i in range(2):
    password.append(random.choice(symbols))

for i in range(passLength-4):
    password.append(random.choice(lower_alphabets + upper_alphabets))
    
random.shuffle(password)
password="".join(password)
print(f"Here is your password: {password}")
