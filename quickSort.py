"""
Quick Sort

Write a program in python to implement the Quick Sort algorithm and 
sort a given list in ascending order. 
"""

#Solution:
def quickSort(list,left,right):
    if left < right:
        partition_pos = partition(list,left,right)
        quickSort(list,left,partition_pos-1)
        quickSort(list,partition_pos+1,right)

def partition(list,left,right):
    i = left
    j = right -1
    pivot = list[right]

    while i < j:
        while i < right and list[i] < pivot:
            i += 1
        while j > left and list[j] >= pivot:
            j -= 1

        if i < j:
            list[i],list[j] = list[j],list[i]

    if list[i] > pivot:
        list[i],list[right] = list[right],list[i] 

    return i

list = [8,3,7,4,1]
quickSort(list,0,len(list)-1)
print(list)

"""
Time Complexity:
    Best Case: O(n log n)
    Average Case: O(n log n)
    Worst Case: O(n^2)
Space Complexity: O(n)
"""
