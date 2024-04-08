# Exercise: Implement the binary search algorithm to find an element in an ordered list.
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

# Example:
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7

print(binary_search(arr, target))  

# Output: 3 (index element = 7)

# Time complexity: O(log n), where 'n' is the number of elements in the list.
# This is because the algorithm repeatedly divides the list in half during each step of the search.
