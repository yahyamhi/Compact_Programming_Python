def sort_dictionaries(dictionaries):
    # Sort the list of dictionaries by the 'make' key
    sorted_dictionaries = sorted(dictionaries, key=lambda x: x['make'])
    return sorted_dictionaries

# Test the function
dictionaries = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
                {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
                {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print(sort_dictionaries(dictionaries))

# Prompt the user for input
string_input = input("Enter a list of dictionaries: ")

# Convert the input string to a list of dictionaries
dictionaries_input = eval(string_input)

# Pass the input to the sort_dictionaries function and print the result
print(sort_dictionaries(dictionaries_input))