class Solution(object):
    def maxProfit(self, prices):
        temp = 0
        max = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)-1):
                if prices[j] < prices[j+1]:
                    temp = prices[j+1]-prices[j]
                    break
                else:
                    break
            max += temp
            temp = 0

        return max
