def sort_tuples(tuples):
    sorted_tuples = sorted(tuples, key=lambda x: x[-1])
    return sorted_tuples

# Test the function
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sort_tuples(sample_list))

# Prompt the user for input
string_input = input("Enter a list of tuples: ")

# Convert the input string to a list of tuples
tuples_input = eval(string_input)

# Pass the input to the sort_tuples function and print the result
print(sort_tuples(tuples_input))