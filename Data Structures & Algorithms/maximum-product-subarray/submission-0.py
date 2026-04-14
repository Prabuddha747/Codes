class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxproduct = max(nums)
        curMin , curMax = 1,1
        for i in nums:
            temp = curMax*i
            curMax = max(i,curMax*i,curMin*i)
            curMin = min(i,curMin*i,temp)
            maxproduct = max(maxproduct,curMax)
        return maxproduct

        