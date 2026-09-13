class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        freq = 1
        operations = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                freq+=1
            else:
                if freq == 1:
                    # print(i)
                    return -1
                operations += (freq+2)//3
                # print(operations)
                freq = 1

        if freq == 1:
            print(i)
            return -1
        operations += (freq+2)//3
        # print(operations) 
                
        return operations

        