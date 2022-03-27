class Solution:

    # BRUTE FORCE SOLUTION
    #     def calculateFib(self, n):
    #         if n == 0: return 0
    #         if n == 1: return 1

    #         return self.calculateFib(n-2) + self.calculateFib(n-1)

    def calculateFib(self, n, fibMap):
        if n == 0:
            return 0
        if n == 1:
            return 1

        if n in fibMap:
            return fibMap[n]

        else:
            fibMap[n] = self.calculateFib(
                n-1, fibMap) + self.calculateFib(n-2, fibMap)
            return fibMap[n]

    def fib(self, n: int) -> int:

        fibMap = {}
        sequenceSum = self.calculateFib(n, fibMap)
        return sequenceSum
