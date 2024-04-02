"""
Pangram Checker

A pangram is a sentence where every letter of the English alphabet 
appears at least once.

Given a string sentence, return true if sentence is a pangram, or false otherwise.
"""

#Solution:
def isPangram(sentence):
    seen = set()
    for char in sentence.lower():
        if char.isalpha():
            seen.add(char)
    return len(seen) == 26

print(isPangram("abcde fghijklmn opqrstuvw xyz"))
