# Runtime = 5 ms
# Memory = 12.62 MB

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2
        g = sorted(num)
        j = len(g)

        if j % 2 == 1:
            return g[j / 2]
        else:
            mid1 = g[j / 2 - 1]
            mid2 = g[j / 2]
            return (mid1 + mid2) / 2.0