#Task: Merge two sorted lists into one sorted list.

def merge_sorted_lists(a, b):
    return sorted(a + b)

#example
print(merge_sorted_lists([2,2,3,3,5], [1,1,2,2,4,4,6]))
# Output: [1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 6]
