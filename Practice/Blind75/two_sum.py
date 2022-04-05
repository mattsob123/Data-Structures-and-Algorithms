def twoSum(self, nums, target):
    nums_map = {}
    
    for i in range(len(nums)):
        calc = target-nums[i]
        if calc in nums_map:
            return[nums_map[calc], i]
        else:
            nums_map[nums[i]] = i
        