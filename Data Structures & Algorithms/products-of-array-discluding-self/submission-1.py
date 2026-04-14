class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        products = [1] * n  # initialize with correct size

        for i in range(n):
            product = 1          # reset once per i
            for j in range(n):
                if j == i:
                    continue
                product *= nums[j]   # multiply by nums, not products
            products[i] = product     # store final product for this i

        return products
        