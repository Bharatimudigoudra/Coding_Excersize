"""Given a list prices, each number is the stock price on that day. You may buy once and sell once on a later day. Write max_profit(prices) to return the highest possible profit. If no profit is possible, return 0.

Examples:
[7, 1, 5, 3, 6, 4] → 5
Buy at 1, sell later at 6.

[7, 6, 4, 3, 1] → 0
[5] → 0
[] → 0

The selling day must come after the buying day. You cannot rearrange the prices.

Start with a working solution. Then try to solve it in one pass and explain its time complexity."""

def max_profit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

print(max_profit([7,1,5,3,6,4]))