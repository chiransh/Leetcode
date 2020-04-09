import collections
class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counter=collections.Counter(arr)
        counter=(dict(counter))
        print(counter)
        count=0
        flag=0
        a=0
        for keys in counter:
            if count!=0:
                if keys==flag+1:
                    a=a+(counter[flag])
            count+=1
            flag=keys
        return a