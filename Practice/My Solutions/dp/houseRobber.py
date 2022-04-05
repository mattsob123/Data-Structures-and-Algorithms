def rob(self, nums):

    max1, max2 = 0, 0

    for house in nums:
        temp = max(max2, (house + max1))
        max1 = max2
        max2 = temp

    return max2
