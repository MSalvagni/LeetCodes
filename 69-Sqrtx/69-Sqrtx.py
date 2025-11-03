# Last updated: 11/3/2025, 4:48:10 PM
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        
        L, R = 1, x // 2

        while L <= R:
            mid = (L + R) // 2
            mid_squared = mid * mid 

            if mid_squared == x:
                return mid
            elif mid_squared < x:
                L = mid + 1
            else:
                R = mid - 1
                
        return R



