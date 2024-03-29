"""
Binary Search

Write a program in python to implement the Binary Search algorithm and 
search for a given key in the provided sorted list of numbers. 
"""

#Solution:
def binarySearch(list,key):
    low = 0
    high = len(list)-1
    key_found = False
    while low <= high and not key_found:
        mid = (low + high) // 2
        if key == list[mid]:
            key_found = True
        elif key > list[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if key_found:
        print("Key is found")
    else:
        print("Key is not found")

list = [2,5,7,9,11,13,17,19,21,33]
key = 7
print(binarySearch(list,key))


"""
Time Complexity:
    Best Case: O(1)
    Average Case: O(log n)
    Worst Case: O(log n)
Space Complexity: O(1)
"""
