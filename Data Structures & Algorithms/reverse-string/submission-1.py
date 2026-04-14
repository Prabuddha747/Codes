class Solution:
    def reverseString(self, s: List[str]) -> None:
        m = s[::-1]
        s.reverse()
        return m