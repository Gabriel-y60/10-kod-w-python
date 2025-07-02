#Task: Write a function to find the second largest number in a list

def second_largest(lst):
    unique = set(lst)
    unique.discard(max(unique))
    return max(unique)

#example
print(second_largest([200,300,400,500,600,700]))
#output: 
