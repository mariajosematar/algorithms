# Exercise: Implement a recursive function to calculate the factorial of a number.
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Example:
n = 5
print(factorial(n))  

# Output: 120 (5!)

# Time complexity: O(n), where 'n' is the number for which the factorial is calculated.
# The algorithm will perform 'n' multiplications in total.
