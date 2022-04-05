def maxProfit(self, prices):
    minVal = max(prices) 
    maxVal = -1
    maxProfit = 0
    
    for price in prices:
        if price < minVal:
            minVal = price
            maxVal = -1 # reset max as we cannot use prior data
        if price > maxVal:
            maxVal = price
            maxProfit = max(maxProfit, maxVal - minVal)
            
    return maxProfit