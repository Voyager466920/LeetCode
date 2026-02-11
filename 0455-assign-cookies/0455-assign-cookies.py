class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        i = 0
        j = 0
        total = 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                j += 1
                total += 1
            elif g[i] > s[j]:
                j += 1
            else:
                i += 1
        return total