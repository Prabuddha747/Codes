class Solution:
    def trap(self, height: List[int]) -> int:
        # min(l,r)-h[i]
        n = len(height)
        if n == 0:
            return 0

        # Arrays to store max height to the left/right
        maxL = [0] * n
        maxR = [0] * n

        # Fill maxL (maximum height to the left of i)
        maxL[0] = height[0]
        for i in range(1, n):
            maxL[i] = max(maxL[i-1], height[i])

        # Fill maxR (maximum height to the right of i)
        maxR[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            maxR[i] = max(maxR[i+1], height[i])

        # Calculate trapped water
        watertrapped = 0
        for i in range(n):
            trapped = min(maxL[i], maxR[i]) - height[i]
            if trapped > 0:
                watertrapped += trapped

        return watertrapped