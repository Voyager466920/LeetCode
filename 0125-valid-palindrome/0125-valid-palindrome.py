class Solution(object):
    def isPalindrome(self, s):
        res = ""
        for ch in s:
            if ch.isalnum():
                res += ch.lower()
        return res == res[::-1]
        