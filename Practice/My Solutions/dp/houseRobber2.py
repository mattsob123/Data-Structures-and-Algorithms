def rob(self, nums):

    if len(nums) < 2:
        return nums[0]

    max1, max2 = 0, 0

    for i in range(1, len(nums), 1):
        temp = max(max1 + nums[i], max2)
        max1 = max2
        max2 = temp

    sol1 = max2
    max1, max2 = 0, 0

    for j in range(0, len(nums)-1, 1):
        temp = max(max1 + nums[j], max2)
        max1 = max2
        max2 = temp

    sol2 = max2

    return max(sol1, sol2)
