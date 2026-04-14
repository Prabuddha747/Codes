class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        lenS = len(strs[0])
        for i in range(lenS):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return s[:i]
            result += strs[0][i]
        return result