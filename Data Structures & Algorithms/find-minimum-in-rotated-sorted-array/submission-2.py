class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = 0
        while l < r:
            m = (l+r) // 2
            res = min(res, nums[l])
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]