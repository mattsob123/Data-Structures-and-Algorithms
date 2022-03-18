class Solution:
    def findDuplicates(self, nums):
        output = []
        
        for num in nums:
            index = abs(num)-1
            
            if nums[index] < 0:
                output.append(index+1)
                
            else:
                nums[index] *= -1
            
        return output
            
        