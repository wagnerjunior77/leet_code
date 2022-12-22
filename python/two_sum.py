class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexes = []
        
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i+1:]):
                if x+y == target:
                    
                    indexes.extend([i, j+i+1])
                    break
            
        return indexes
    
instance = Solution()

print(instance.twoSum([3,3], 6))



        
