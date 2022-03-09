class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        pFirst, pLast = 0, len(nums)-1

        output = []

        while pLast >= pFirst:

            firstNum = abs(nums[pFirst])
            lastNum = abs(nums[pLast])

            if lastNum > firstNum:
                square = lastNum * lastNum
                output.append(square)

                pLast -= 1

            else:
                square = firstNum * firstNum
                output.append(square)

                pFirst += 1

        return output[::-1]
