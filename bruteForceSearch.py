# Ejercicio: Dado un conjunto de números, encuentra el par de números cuya suma sea igual a un objetivo dado.

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Ejemplo
nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target)) 

# Output: [0, 1] (índices de los números 2 y 7)

# Complejidad temporal: O(n^2), donde n es el número de elementos en la lista.
# Esto se debe a que el algoritmo realiza un bucle anidado para cada elemento en la lista.