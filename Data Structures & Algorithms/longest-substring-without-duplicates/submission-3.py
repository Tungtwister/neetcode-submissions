class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charIdx = {}
        i = 0
        res = 0

        for j in range(len(s)):
            if s[j] in charIdx:
                i = max(charIdx[s[j]]+1, i)
            charIdx[s[j]] = j
            res = max(res, j - i + 1)
        
        return res

