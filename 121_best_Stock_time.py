class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
    
def main():
    prices = [1]
    print(Solution().maxProfit(prices))  # Output: 2
if __name__ == "__main__":
    main()                