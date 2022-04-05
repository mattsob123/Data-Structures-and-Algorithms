class Solution:
    def twoSum(self, nums, target):
        
        hashmap = {} # hashmap of prior elements
        
        for i, n in enumerate(nums): # index | value
            
            diff = target - n
            
            if diff in hashmap:
                return [hashmap[diff], i]
            
            else:
                hashmap[n] = i