class Solution(object):
    def hammingWeight(self, n):
        length = 0

        while n != 0:
            if n % 2 == 1:
                length += 1
            n /= 2
        return length

        