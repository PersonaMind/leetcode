# Runtime = 0 ms
# Memory = 12.60 MB

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()

        return len(s[-1])
