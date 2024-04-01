"""
Two Sum

Given a list of integers nums and an integer target, write a function in python to 
return indices of the two numbers such that they add up to target.

Example input/Output:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Input: nums = [3,2,4], target = 6
Output: [1,2]
"""

#Solution:
def twoSum(nums, target):
        index_map = {}
        for i in range(len(nums)):
            index_map[nums[i]] = i
        for i in range(0,len(nums)):
            compliment = target - nums[i]
            if compliment in index_map and index_map[compliment] != i:
                return [i,index_map[compliment]]
            else:
                return "Target not found"
        
nums = [2,7,11,15]
target = 19
print(twoSum(nums, target))
