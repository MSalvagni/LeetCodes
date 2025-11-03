# Last updated: 11/3/2025, 5:19:32 PM
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        end = 0

        while x > end:
           end = (end * 10) + (x%10)
           x //= 10
        return x == end or x == end//10
