class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        count_start=0
        length=len(height)
        count_end=length-1
        area=min(height[count_start],height[count_end])*(count_end-count_start)            
        for i in range(length):
            if height[count_start]>height[count_end]:
                count_end-=1
            else:
                count_start+=1
            area_new=min(height[count_start],height[count_end])*(count_end-count_start)
            if area_new>area:
                area=area_new
            if count_end==count_start:
                return area
        return area
s=Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))