class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = set()
        for s in nums:
            if s in num:
                return True
            num.add(s)
        return False