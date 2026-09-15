class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMinPrice = None
        currMaxProfit = 0
        currProfit = 0
        for i in range(len(prices)):
            price = prices[i]
            if (currMinPrice is None):
                currMinPrice = price
            else:
                if price - currMinPrice >= currProfit:
                    currProfit = price - currMinPrice
                    if currProfit > currMaxProfit:
                        currMaxProfit = currProfit
                elif price < currMinPrice and i < len(prices) - 1:
                    currMinPrice = price
                    currProfit = 0

        return currMaxProfit
