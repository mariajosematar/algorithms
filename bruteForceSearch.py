# Exercise: Given a set of numbers, find the pair of numbers whose sum equals a given objective.
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Example:
nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target)) 

# Output: [0, 1] (indices of numbers 2 y 7)

# Time complexity: O(n^2), where 'n' is the number of elements in the list.
# When the number of elements in a list is 'n', the algorithm performs a nested loop 'n' times.
