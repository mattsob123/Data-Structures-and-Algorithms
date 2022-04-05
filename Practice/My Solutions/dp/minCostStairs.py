def minCostClimbingStairs(self, cost):
    start = len(cost)-1
    cost.append(0)
    cost.append(0)  # signifies the completed staircase

    for i in range(start, -1, -1):
        cost[i] = cost[i] + min(cost[i+1], cost[i+2])

    return min(cost[0], cost[1])
