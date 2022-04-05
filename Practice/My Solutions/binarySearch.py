import math
nums = [1, 4, 7, 8, 9, 10, 11, 15]


def binarySearch(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:

        index = math.floor((left+right)/2)

        if nums[index] < target:
            left = index + 1
        elif nums[index] > target:
            right = index - 1
        else:
            return index

    return -1


print(binarySearch(nums, 15))
