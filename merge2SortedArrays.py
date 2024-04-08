"""
Merge 2 Sorted Arrays/Lists

Write a program in python that takes two sorted integer arrays/lists
as input and merge them so that the items are in a non-descending order.
"""

#Solution:
def mergeSortedArrays(list1, list2):
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1
    
    mergedList = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            mergedList.append(list1[i])
            i += 1
        else:
            mergedList.append(list2[j])
            j += 1

    while i < len(list1):
        mergedList.append(list1[i])
        i += 1

    while j < len(list2):
        mergedList.append(list2[j])
        j += 1
            
    return mergedList

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
print(mergeSortedArrays(list1, list2))
