class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) -1:
            farthest = 0
            for i in range(l, r+1):
                #find the farthest they can jump
                farthest = max(farthest, i + nums[i])
            #create a window of the options where they land and jump from
            #find the farthest jump possible for that window
            l = r + 1
            r = farthest
            res += 1
        return res