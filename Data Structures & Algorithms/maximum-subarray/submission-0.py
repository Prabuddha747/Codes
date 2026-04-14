class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = 0
        maxsum=nums[0]
        for n in nums:
            if sums<=0:
                sums=0
            sums+=n
            maxsum=max(maxsum,sums)
        return maxsum