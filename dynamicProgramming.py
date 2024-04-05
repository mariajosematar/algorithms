# Ejercicio: Dado un conjunto de monedas con valores [1, 5, 10, 25] y una cantidad, encuentra el número mínimo de monedas necesarias para formar esa cantidad.

def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount]

# Ejemplo
coins = [1, 5, 10, 25]
amount = 48

print(min_coins(coins, amount))  

# Output: 6 (48 = 25 + 10 + 10 + 1 + 1 + 1)

# Complejidad temporal: O(n * m), donde n es la cantidad y m es el número de tipos de monedas.
# Esto se debe a que el algoritmo llena una matriz de tamaño n * m y cada celda de la matriz se llena una vez. 