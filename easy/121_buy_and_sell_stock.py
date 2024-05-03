from typing import List


def max_profit(prices: List[int]) -> int:
    if all(prices[x] >= prices[x + 1] for x in range(len(prices) - 1)):
        return 0
    max_profit = 0
    min_price = prices[0]
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit



prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]
prices3 = []

profit = max_profit(prices1)
assert profit == 5
profit = max_profit(prices2)
assert profit == 0
