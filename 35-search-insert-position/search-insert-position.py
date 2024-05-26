class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:        
        for i in range(len(nums)):
            curr = nums[i]            
            if curr >= target :
                return i            
        return len(nums)