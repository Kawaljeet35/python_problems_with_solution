"""
Valid Anagram

Write a program in python to check if two strings are 
anagram or not.
The program should return a boolean.
"""

#Solution:
def isAnagram(str1,str2):
    sorted_str1 = sorted(str1.lower())
    sorted_str2 = sorted(str2.lower())
    return sorted_str1 == sorted_str2

print(isAnagram("heart","earth"))
