"""
Selection Sort

Write a program in python to implement the Selection Sort algorithm and 
sort a given list in ascending order. 
"""

#Solution:
def selectionSort(list):
    for i in range(len(list)-1):
        min_index = i
        for j in range(i+1,len(list)):
            if list[j] < list[min_index]:
                min_index = j
        if list[i] != list[min_index]:
            list[i], list[min_index] = list[min_index], list[i]
    return list

list = [8,3,7,4,1,1,1]
print(selectionSort(list))

"""
Time Complexity:
    Best Case: O(n^2)
    Average Case: O(n^2)
    Worst Case: O(n^2)
Space Complexity: O(1)
"""
