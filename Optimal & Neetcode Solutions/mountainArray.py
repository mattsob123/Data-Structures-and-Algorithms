sampleMountain = [0, 10, 5, 2]


def linearScan(arr):
    # sub-optimal O(n) time complexity

    i = 1
    while arr[i-1] < arr[i]:
        i += 1
    return i-1



def binaryScan(arr):
    # optimal solution, O(log n) time complexity


    left, right = 0, len(arr)-1
        
    while left < right:
        
        mid = left + ((right - left) // 2)
        
        if arr[mid] < arr[mid+1]:
            left = mid+1
        
        else:
            right = mid
        
    return left

print(linearScan(sampleMountain))
print(binaryScan(sampleMountain))
