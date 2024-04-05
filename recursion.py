# Ejercicio: Implementa una función recursiva para calcular el factorial de un número.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Ejemplo
n = 5
print(factorial(n))  

# Output: 120 (5!)

# Complejidad temporal: O(n), donde n es el número para el que se calcula el factorial.
# Esto se debe a que el algoritmo realizará n multiplicaciones en total.