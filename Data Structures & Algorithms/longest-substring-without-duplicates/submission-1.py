class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        r, l = 0, 0
        sets = set()
        count = 0
        max_count = 0

        while l < len(s):
            if s[l] not in sets:
                sets.add(s[l])
                l += 1
            else:
                count = len(sets)
                max_count = max(count, max_count)
                sets.clear()
                r += 1
                l = r
        # Final check in case longest substring is at the end
        max_count = max(len(sets), max_count)
        return max_count