"""
Merge Sort

Write a program in python to implement the Merge Sort algorithm and 
sort a given list in ascending order. 
"""

#Solution:
def mergeSort(list):
    if len(list)>1:
        mid = len(list) // 2
        left_list = list[:mid]
        right_list = list[mid:]
        mergeSort(left_list)
        mergeSort(right_list)
        i = 0
        j = 0
        k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i += 1
                k += 1
            elif left_list[i] > right_list[j]:
                list[k] = right_list[j]
                j += 1
                k += 1
        while i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1
    return list

list = [8,3,7,4,1]
print(mergeSort(list))

"""
Time Complexity:
    Best Case: O(n log n)
    Average Case: O(n log n)
    Worst Case: O(n log n)
Space Complexity: O(n)
"""
