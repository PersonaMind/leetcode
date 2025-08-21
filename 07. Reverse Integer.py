# Runtime = 15 ms
# Memory = 12.26 MB

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        string = str(abs(x))
        reversed_string = string[::-1]
        result = int(reversed_string)

        if result < -2**31 or result > 2**31:
            return 0
        return sign * result