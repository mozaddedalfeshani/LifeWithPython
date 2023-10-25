class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 2147483647  # create a min value with max value
        max = 0
        # we are checking each value with min, coz next not be min

        for i in range(len(prices)):
            if prices[i] <= min:
                min = prices[i]

            if prices[i] - min > max:
                max = prices[i] - min

        return max
