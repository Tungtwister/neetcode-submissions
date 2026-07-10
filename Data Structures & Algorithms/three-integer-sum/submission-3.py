class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx, a in enumerate(nums):
            if a > 0:
                break
            #iterate through nums for first value
            if idx > 0 and a == nums[idx-1]: #if duplicate value then skip forward
                continue
            
            #basically becomes two sum 2
            l, r = idx + 1, len(nums) - 1

            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    #a solution found gets added to res and l and r continue
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l < r:
                        l+=1

        return res