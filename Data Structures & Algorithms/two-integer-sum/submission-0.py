class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for idx, i in enumerate(nums):
            diff = target - i
            if diff in temp:
                return [temp[diff], idx]
            temp[i] = idx 