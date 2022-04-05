class Solution:
    def majorityElement(self, nums):

        count = 0
        majority = 0

        for vote in nums:
            if count == 0:
                majority = vote
                count += 1

            elif vote == majority:
                count += 1

            else:
                count -= 1
        
        return majority


zoom = Solution()

votes = ["bob", "bob", "bob", "jim", "jim", "jim", "bob", "john", "john"]

print(zoom.majorityElement(votes))
