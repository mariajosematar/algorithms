# Exercise: Given a set of coins with values ​​[1, 5, 10, 25], find the combination of coins with the smallest possible amount to give a change of n cents.
def make_change(coins, amount):
    coins.sort(reverse=True)
    change = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            change.append(coin)
    return change

# Example:
coins = [1, 5, 10, 25]
amount = 48


print(make_change(coins, amount))  

# Output: [25, 10, 10, 1, 1, 1]

# Time complexity: O(n), where 'n' is the number of coins needed to make the change.
# This is because the algorithm will iterate over the coin list once for each coin needed.
