# Ejercicio: Implementa el algoritmo de búsqueda binaria para encontrar un elemento en una lista ordenada.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Ejemplo
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7

print(binary_search(arr, target))  

# Output: 3 (el índice del elemento 7)

# Complejidad temporal: O(log n), donde n es el número de elementos en la lista.
# Esto se debe a que el algoritmo divide repetidamente la lista a la mitad en cada paso de la búsqueda.