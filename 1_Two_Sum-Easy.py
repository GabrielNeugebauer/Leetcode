#This function return indices of two numbers such that they add up to target. The numbers will be passed in the array nums and we may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
   def twoSum(self, nums, target):
        """nums: List[int]
        target: int
        -> List[int]"""
        #Saving memory but using 10x more processing
        """
        for i,num in enumerate(nums):
            if target-num in nums[i+1:]:
               return [i, nums[i+1:].index(target-num)+i+1]"""
        #Using 330KB more of memory, but running 10x faster
        seen = {}
        for i, value in enumerate(nums):
           diff = target - nums[i]
           if diff in seen:
               return [seen[diff],i]
           seen[value] = i 