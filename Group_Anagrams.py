from collections import defaultdict 
class Solution(object):
    def groupAnagrams2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dicty=defaultdict(list)
        str_list=[]
        for i in range(len(strs)):
            split_chars=[i for i in strs[i].encode("utf-8")]
            sorted_string= ''.join(sorted(split_chars))
            if sorted_string not in dicty.keys():
                dicty[(sorted_string)].append(strs[i])
            if sorted_string in dicty.keys():
                dicty[sorted_string].append(strs[i])
        for keys in dicty:
            str_list.append(dicty[keys])
        return str_list
    
    def groupAnagrams(self, strs):
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()
