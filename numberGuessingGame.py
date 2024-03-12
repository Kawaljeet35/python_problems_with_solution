"""
Number Guessing Game

Write a program in python which replicates the number guessing game in real life.

The program should generate a random number forehand and prompt the user to 
guess a number between 1 and 100. Depending upon the user guess, the program should suggest
the user to either guess a lower or bigger number.
The program should keep a count on the number of attempts a user takes to guess the 
correct number.

Example Input/Output:

Guess a number between 1 and 100: 78
Guess a smaller number: 4
Guess a bigger number: 33
Guess a bigger number: 67
Guess a smaller number: 32
Guess a bigger number: 62
Congratulations! You guessed the number in 6 attempts.
"""


#Solution:
import random

number = random.randint(1,100)
user_guess = int(input("Guess a number between 1 and 100: "))
num_attempts = 0

while(user_guess!=number):
    if(user_guess > number):
        num_attempts += 1
        user_guess = int(input("Guess a smaller number: "))
    elif(user_guess < number):
        num_attempts += 1
        user_guess = int(input("Guess a bigger number: "))

num_attempts += 1
print(f"Congratulations! You guessed the number in {num_attempts} attempts.")
