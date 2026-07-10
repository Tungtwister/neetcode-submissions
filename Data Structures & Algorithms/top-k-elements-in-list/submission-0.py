class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        res = sorted(zip(freq.values(),freq.keys()), reverse = True)
        topk = res[:k]
        return list(top[1] for top in topk)