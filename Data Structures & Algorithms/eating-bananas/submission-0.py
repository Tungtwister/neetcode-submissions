class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #the idea for binary search is the start in the middle 
        # with range being 1 to the largest pile value
        #if the rate of k is too slow we then look at the right partition
        #if rate of k is too fast then we look into the left partition
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res