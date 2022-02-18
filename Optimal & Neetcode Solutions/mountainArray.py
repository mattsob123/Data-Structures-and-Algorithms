sampleMountain = [0, 10, 5, 2]


def linearScan(arr):
    # sub-optimal O(n) time complexity

    i = 1
    while arr[i-1] < arr[i]:
        i += 1
    return i-1


print(linearScan(sampleMountain))
