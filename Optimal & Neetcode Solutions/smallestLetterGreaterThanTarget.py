import math


letters = ["a", "f", "m", "q", "w"]


def smallestLetter(letters, target):
    left, right = 0, len(letters)-1

    while left < right:

        index = math.floor((left+right)/2)

        if letters[index] <= target:
            left = index + 1
        else:
            right = index

    print(left)
    return letters[left % len(letters)]


print(smallestLetter(letters, "n"))
