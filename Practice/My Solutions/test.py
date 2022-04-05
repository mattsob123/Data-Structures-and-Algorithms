arr = [769082435, 210437958, 673982045, 375809214, 380564127]

arrSum = sum(arr)
minSum = arrSum
maxSum = 0

print(minSum)
print(arrSum-arr[0])

for number in arr:
    curSum = arrSum - number
    if curSum > maxSum:
        maxSum = curSum

    elif curSum < minSum:
        minSum = curSum

    print(minSum, maxSum)
