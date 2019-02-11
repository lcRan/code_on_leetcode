def maxProfit(prices):
    length = len (prices)
    if length == 0:
        return 0
    max = 0
    min = prices[0]
    for i in range (length):
        if prices[i] < min:
            min = prices[i]
        if prices[i] - min > max:
            max = prices[i] - min

    return max

price = [7, 1, 5, 3, 6, 4]
print (maxProfit(price))