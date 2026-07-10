class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #has to be the same length to even be an anagram
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0) #add a count to the key for S
            countT[t[i]] = 1 + countT.get(t[i],0) # add a count to T

        return countS == countT #if has the same letters it should match

        #runtime O(n + m) because has to iterate through s and t once
        #space: O(1) for two dicts