class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = set(nums)
        if len(nums) != len(numbers):
            return True
        return False