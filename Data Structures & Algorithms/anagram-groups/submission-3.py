class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping character count to list of anagrams
                                #default dict to deal if key is new and doesn't exist yet

        for s in strs:
            count = [0] * 26 #list of 26 0s for a to z

            for c in s:
                #this is done instead of sorting the word then using that as the key 
                #because sorting would be nlogn time complexity while this also iterates through the string once to categorize it
                count[ord(c) - ord("a")] += 1 #ascii value of letter - ascii value of "a"
            res[tuple(count)].append(s) #append string that matches the tuple count

        return list(res.values())

    #time O(m * n)
    #space O(m)