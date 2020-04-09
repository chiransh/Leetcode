class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        a=s.strip()
        if len(a)==0:
            return 1

        dic={}
        max_val=0
        for i in s:
            if max_val<len(dic):
                max_val=len(dic)
            if i not in dic:
                dic[i]=1
            else:   
                dic={i:1}
            





        return max_val
s=Solution()
s.lengthOfLongestSubstring("c")