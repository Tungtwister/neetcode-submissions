class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in strs:
            temp = ''.join(sorted(i))
            anagrams[temp].append(i)
        return list(anagrams.values())