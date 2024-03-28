"""
Insertion Sort

Write a program in python to implement the Insertion Sort algorithm and 
sort a given list in ascending order. 
"""

#Solution:
def insertionSort(list):
    for i in range(1,len(list)):
        current_element = list[i]
        pos = i
        while current_element < list[pos-1] and pos > 0:
            list[pos] = list[pos-1]
            pos -= 1
        list[pos] = current_element
    return list

list = [8,3,7,4,1]
print(insertionSort(list))

"""
Time Complexity:
    Best Case: O(n)
    Average Case: O(n^2)
    Worst Case: O(n^2)
Space Complexity: O(1)
"""
