#Task: Write a function that takes a sentence as input and returns the sentence with the word order reversed.

def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

#example
print(reverse_sentence("nissan patrol is cool"))
# Output: "cool is patrol nissan"


