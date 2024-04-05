# Ejercicio: Dado un conjunto de monedas con valores [1, 5, 10, 25], encuentra la combinación de monedas con la menor cantidad posible para dar un cambio de n centavos.

def make_change(coins, amount):
    coins.sort(reverse=True)
    change = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            change.append(coin)
    return change

# Ejemplo
coins = [1, 5, 10, 25]
amount = 48


print(make_change(coins, amount))  

# Output: [25, 10, 10, 1, 1, 1]

# Complejidad temporal: O(n), donde n es el número de monedas necesarias para dar el cambio.
# Esto se debe a que el algoritmo iterará sobre la lista de monedas una vez para cada moneda necesaria.