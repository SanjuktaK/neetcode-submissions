class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def helper(i, nums):
            if i >= len(nums) - 1:
                return True
            if nums[i] == 0:
                return False
            if i in memo:
                return memo[i]
            for j in range(1, nums[i] + 1):
                if helper(i + j, nums):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        
        return helper(0, nums)