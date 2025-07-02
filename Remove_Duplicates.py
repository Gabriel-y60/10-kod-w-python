#Task: Write a function to remove duplicates from a list without using set() directly in the return statement.

def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

#example
print(remove_duplicates([1,1,2,3,3,3,4,5,6,6,77,77,8]))
# Output: [1, 2, 3, 4, 5, 6, 77, 8]
