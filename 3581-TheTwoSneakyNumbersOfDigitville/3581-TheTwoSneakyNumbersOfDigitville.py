# Last updated: 10/31/2025, 12:54:27 AM
class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()
        duplicate = []

        for num in nums:
            if num in seen:
                duplicate.append(num)
            else: 
                seen.add(num)
        return duplicate