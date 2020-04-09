import re
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str=str.strip()
        a=re.findall(r'^[+ \-]?\d+',str)
        try:
            a = int(''.join(a))
            MAX = 2147483647
            MIN = -2147483648
            if a > MAX:
                return MAX
            if a < MIN: 
                return MIN
            return a
        except:
            return 0
        
s=Solution()
print(s.myAtoi("with words"))
print(s.myAtoi("-91283472332"))