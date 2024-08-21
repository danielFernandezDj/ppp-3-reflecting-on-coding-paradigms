# Functional Programming Solution
from functools import reduce

# Function to flatten and sort an array of integers
def flatten_and_sort(arr):
    # Flattening the array using reduce and lambda
    flattened = reduce(lambda x, y: x + y, arr)
    # Sorting the flattened array
    return sorted(flattened)

# Example usage:
nested_array = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
sorted_array = flatten_and_sort(nested_array)
print(sorted_array)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Reflection:
# 1. How does this solution ensure data immutability?
# - The solution ensures data immutability by not modifying the input array directly.
# Instead, it returns a new array that is a flattened and sorted version of the original array.
#
# 2. Is this solution a pure function? Why or why not?
# - Yes, this solution is a pure function because it produces the same output given the same input,
# and it does not cause any side effects.
#
# 3. Is this solution a higher-order function? Why or why not?
# - Yes, this solution uses a higher-order function (`reduce`), which takes a lambda function as an argument.
#
# 4. Would it have been easier to solve this problem using a different programming style?
# - It could have been more straightforward to use an imperative style with loops for those
# unfamiliar with functional programming. However, this solution demonstrates the power of functional
# programming in handling such tasks concisely.
#
# 5. Why in particular is functional programming a helpful paradigm when solving this problem?
# - Functional programming is helpful in this context because it allows for concise, clear,
# and declarative code, making it easier to handle complex transformations like flattening and sorting.
