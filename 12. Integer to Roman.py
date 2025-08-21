# Runtime = 7 ms
# Memory = 12.41 MB

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        roman = ""
        for i, v in enumerate(val):
            while num >= v:
                roman += syms[i]
                num -= v
        return roman