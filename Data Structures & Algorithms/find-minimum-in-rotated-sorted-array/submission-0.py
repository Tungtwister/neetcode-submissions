class Solution:
    def findMin(self, nums: List[int]) -> int:
        a = 0
        b = len(nums)-1
        min_ele = float("inf")
        while a < b:
            mid = a + (b - a) // 2
            min_ele = min(min_ele, nums[mid])
            
            if nums[mid] > nums[b]:
                a = mid + 1
            else:
                b = mid - 1
        
        return min(min_ele, nums[a])
        
