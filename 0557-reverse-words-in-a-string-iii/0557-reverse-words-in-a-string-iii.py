class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        chars = s.split(" ")
        for ch in chars:
            res.append(ch[::-1])
        return " ".join(res)
        
        