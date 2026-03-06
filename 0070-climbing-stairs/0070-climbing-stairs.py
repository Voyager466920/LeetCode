class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one = 1
        two = 1

        for _ in range(n-1):
            tmp = two
            two = one + two
            one = tmp
        return two
        