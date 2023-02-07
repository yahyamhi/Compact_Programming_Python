def convert_to_lists(strings):
    # Convert the strings to lists using map and list
    lists = list(map(list, strings))
    return lists

# Test the function
strings = ['abc', 'def', 'ghi']
print(convert_to_lists(strings))

# Prompt the user for input
string_input = input("Enter a list of strings: ")

# Convert the input string to a list of strings
strings_input = eval(string_input)

# Pass the input to the convert_to_lists function and print the result
print(convert_to_lists(strings_input))