class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = set()
        for i in nums:
            if i in num:
                num.remove(i)
            else:
                num.add(i)
        return list(num)[0]
        