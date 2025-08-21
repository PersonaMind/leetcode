class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        numerals = {'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}
        y = 0
        n = len(s)        

        for i in range(n):
            if i + 1 < n and numerals[s[i]] < numerals[s[i + 1]]:
                y -= numerals[s[i]]
            else:
                y += numerals[s[i]]

        return y