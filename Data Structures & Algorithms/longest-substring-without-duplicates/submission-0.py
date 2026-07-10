class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup = {}
        l = 0
        ans = 0
        for r in range(len(s)):
            if s[r] in dup:
                l = max(dup[s[r]]+1, l)
            dup[s[r]] = r

            ans = max(ans, r - l + 1)
        return ans
