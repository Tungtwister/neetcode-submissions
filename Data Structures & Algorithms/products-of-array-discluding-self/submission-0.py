class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_cnt = 0
        for i in nums:
            if i == 0:
                zero_cnt += 1
            else:
                product *= i
        if zero_cnt > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for idx, j in enumerate(nums):
            if zero_cnt > 0:
                if j == 0:
                    res[idx] = product
                else:
                    res[idx] = 0
            else:
                res[idx] = product//j
                
        return res