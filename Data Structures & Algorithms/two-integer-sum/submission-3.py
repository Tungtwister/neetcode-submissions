class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in idxs:
                return [idxs[rem], i]
            idxs[nums[i]] = i
        