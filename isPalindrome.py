"""
Program to check if a string is palindrome.

Write a python program to check if a string is palindrome.

Example output:

abcde is not palindrome.
abcba is palindrome.
"""

#Solution:
def isPalindrome(string):
    string = string.lower()
    return string == string[::-1]

def checkPalindrome(string):
    if isPalindrome(string):
        print(f"{string} is palindrome.")
    else:
        print(f"{string} is not palindrome.")

checkPalindrome("abcde")
checkPalindrome("abcba")
