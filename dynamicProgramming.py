# Exercise: Given a set of coins with values ​​[1, 5, 10, 25] and a quantity, find the minimum number of coins needed to form that quantity.
def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount]

# Example:
coins = [1, 5, 10, 25]
amount = 48

print(min_coins(coins, amount))  

# Output: 6 (48 = 25 + 10 + 10 + 1 + 1 + 1)

# Time complexity: O(n * m), where 'n' is the quantity and m is the number of types of coins.
# This is because the algorithm fills an array of size n*m and each cell of the array is filled once.
