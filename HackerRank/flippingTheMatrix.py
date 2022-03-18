def flippingMatrix(matrix):
    # Write your code here

    # iterate through top left quad

    maximumSum = 0
    mLen = len(matrix)
    qLen = len(matrix)//2

    for r in range(qLen):
        for c in range(qLen):

            print(c)
            maximumSum += max(matrix[r][c], max(matrix[mLen-r-1][c],            # corresponding from botleft
                                                # corresponding from botright
                                                matrix[mLen-r-1][mLen-c-1],
                                                matrix[r][mLen-c-1]))   # corresponding from topright

    return maximumSum
