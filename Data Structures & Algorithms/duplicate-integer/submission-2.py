class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        IfInset = set()
        for i in nums:
            if i in IfInset:
                return True
            else:
                IfInset.add(i)
        return False

         