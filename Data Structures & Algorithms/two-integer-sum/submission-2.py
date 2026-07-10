class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {} #dictionary to track when a value occurs

        for idxs, i in enumerate(nums):
            rem = target - i
            if rem in idx:
                return [idx[rem], idxs]
            idx[i] = idxs