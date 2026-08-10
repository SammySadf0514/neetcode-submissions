class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = prices[0]
        profit = 0
        for i in prices:
            if i < min_value:
                min_value = i
            elif i > min_value:
                if (i - min_value) > profit:
                    profit = i - min_value
        return profit
        