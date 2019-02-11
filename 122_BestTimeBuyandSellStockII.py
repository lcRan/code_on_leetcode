def maxProfit(prices):
    max = 0
    for i in range (1, len(prices)):
        if prices[i] > prices[i-1]:
            max += prices[i] - prices[i - 1]
    return max

prices = [1, 2, 3, 9, 6, 4]
print (maxProfit(prices))