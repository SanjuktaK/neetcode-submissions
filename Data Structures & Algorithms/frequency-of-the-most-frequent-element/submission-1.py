class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        count = 0
        summ = 0

        for r in range(len(nums)):
            summ += nums[r]
            cost = (r-l+1)*nums[r]-summ
            while cost > k:
                summ -= nums[l]
                l +=1
                cost = (r-l+1)*nums[r]-summ
                
            
            count = max(count,(r-l+1))
        return count
            

        
            

        