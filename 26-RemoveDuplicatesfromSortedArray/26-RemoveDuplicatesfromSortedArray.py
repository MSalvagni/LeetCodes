# Last updated: 11/3/2025, 3:15:01 PM
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        unique_nums = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[unique_nums]:
                unique_nums += 1 
                nums[unique_nums] = nums[i]
        return unique_nums + 1




