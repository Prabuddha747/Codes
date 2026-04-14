class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max_area=0
        # for i in range(len(heights)):
        #     for j in range(i+1,len(heights)):
        #         area = min(heights[i],heights[j])*(j-i)
        #         max_area = max(max_area,area)
        # return max_area

        max_area=0
        l,r = 0,len(heights)-1
        while l<r:
            area = min(heights[l],heights[r])*(r-l)
            max_area = max(max_area,area)
            if(heights[l]<heights[r]):
                l+=1;
            else:
                r-=1
        return max_area

        