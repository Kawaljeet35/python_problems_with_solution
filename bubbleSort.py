"""
Bubble Sort

Write a program in python to implement the Bubble Sort algorithm and 
sort a given list in ascending order. 
"""

#Solution:
def bubbleSort(list):
    for i in range(len(list) - 1):
        swapped = False
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped = True
        if not swapped:
            break
    return list

list_a = [8, 3, 4, 7, 1, 1]
print(bubbleSort(list_a))


"""
Time Complexity:
    Best Case: O(n)
    Average Case: O(n^2)
    Worst Case: O(n^2)
Space Complexity: O(1)
"""

 
