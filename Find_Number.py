#Task: Given a list of numbers from 1 to n with one number missing, find the missing number.

def find_missing_number(lst):
    n = len(lst) + 1
    return n * (n + 1) // 2 - sum(lst)

#example
print(find_missing_number([1,2,3,4,6,7,8,9]))
# Output: 5
