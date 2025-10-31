# Last updated: 10/31/2025, 12:54:26 AM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        for i, num in enumerate(nums):
            num_to_add = target - num
            if num_to_add in num_to_index:
                return [num_to_index[num_to_add], i]
            num_to_index[num] = i
