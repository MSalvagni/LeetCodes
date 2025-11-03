# Last updated: 11/3/2025, 4:43:42 PM
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.numRange = [0]

        for num in nums:
            self.numRange.append(self.numRange[-1] + num)



    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        return self.numRange[right+1] - self.numRange[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)