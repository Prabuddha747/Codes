class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        max_area=0
        for i in range(len(heights)):
            for j in range(len(heights)):
                area = min(heights[i],heights[j])*(j-i)
                max_area = max(max_area,area)
        return max_area

        