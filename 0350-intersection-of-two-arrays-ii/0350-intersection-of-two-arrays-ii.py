class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        seen = Counter(nums1)
        res = []
        for n in nums2:
            if n in seen and seen[n] > 0:
                seen[n] -= 1
                res.append(n)
        return res
