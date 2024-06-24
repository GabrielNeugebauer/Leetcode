class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #63ms and 17.84MB, O(N)
        i = 0

        for num in nums:
            if i < 1 or num > nums[i - 1]:
                nums[i] = num
                i += 1

        return i