class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #39ms and 16.25MB, O(N)
        k = 0
        for i in range(len(nums)):
            if (nums[i] != val):
                nums[k] = nums[i]
                k += 1
        return k