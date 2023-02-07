def word_count(s):
    words = s.split()
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    return word_counts

# Prompt the user for input
s = input("Enter a string: ")

# Pass the input to the word_count function and print the result
print(word_count(s))