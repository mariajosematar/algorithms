# Exercise: Given a list of unordered numbers, sort it from least to greatest using the selection algorithm.
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example:
unsorted_list = [64, 25, 12, 22, 11]
sorted_list = selection_sort(unsorted_list)

print(sorted_list)  

# Output: [11, 12, 22, 25, 64]
