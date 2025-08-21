# Runtime = 0 ms
# Memory = 13.15 MB

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numToIndex = {}

        for i in range(len(nums)):
            amount = target - nums[i]
            if amount in numToIndex:
                return numToIndex[amount], i

            numToIndex[nums[i]] = i
