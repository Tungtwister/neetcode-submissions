class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        #Counter creates a dictionary which counts the frequencies
        #example, key = apples, value = 2 counts amount of times apple appears