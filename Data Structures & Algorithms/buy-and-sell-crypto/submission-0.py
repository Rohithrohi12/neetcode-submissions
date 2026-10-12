class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float('Inf') # To take first value of arr as minimum
        max_profit = 0

        for price in prices:
            if price < min_val:
                min_val = price

            profit = price-min_val
            if profit > max_profit:
                max_profit = profit
            
        return max_profit

        