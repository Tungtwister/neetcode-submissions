class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}

        for idx, i in enumerate(nums):
            rem = target - i
            if rem in idxs:
                return [idxs[rem], idx]
            idxs[i] = idx
