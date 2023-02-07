import numpy as np
import matplotlib.pyplot as plt

# Plotting pie and bar charts for Question 01 and Question 02

print("\n\n-------------- Question 01 --------------\n")


# Create an array of values 10 to 48
original = np.arange(10, 49)
reversed_array = original[::-1]

print("Original Vector:")
print(original)
print("Reverse Vector:")
reverse = original[::-1]
print(reverse)

# Plot original array as a bar plot
plt.bar(np.arange(len(original)), original, label='Original')

# Plot reversed array as a bar plot
plt.bar(np.arange(len(reversed_array)), reversed_array, label='Reversed', bottom=original)

plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Original and Reversed Vectors as Bar Plots")
plt.legend()
plt.show()

plt.pie([original.sum(), reversed_array.sum()], labels=['Original', 'Reversed'],
        colors=['b', 'r'], startangle=90, counterclock=False,
        wedgeprops={'alpha':0.5})

plt.title("Difference between Original and Reversed Vectors")
plt.legend()
plt.show()

print("\n\n-------------- Question 02 --------------\n")

# Generate a 5x5 random array
a = np.random.random((5, 5))
print("Original Array:\n{}".format(a))

# Find the minimum and maximum values in the array
amin, amax = a.min(), a.max()
print("\nMinimum and Maximum Values:\nMin: {}\nMax: {}".format(amin, amax))

# Create a bar plot of the minimum and maximum values
values = [amin, amax]
labels = ['Minimum', 'Maximum']
plt.bar(labels, values)
plt.xlabel('Value Type')
plt.ylabel('Value')
plt.title('Minimum and Maximum Values')
plt.show()

# Create a pie chart of the minimum and maximum values
values = [amin, amax]
labels = ['Minimum', 'Maximum']
plt.pie(values, labels=labels, startangle=90, counterclock=False)
plt.axis('equal')
plt.title('Minimum and Maximum Values')
plt.show()

print("\n\n-------------- Question 03 --------------\n")

# Normalize the original array
anorm = (a - amin) / (amax - amin)
print("After normalization:\n{}".format(anorm))

print("\n\n-------------- Question 04 --------------\n")

# Generate two random arrays: 5x3 and 3x2
x = np.random.random((5, 3))
print("5x3 array:\n{}".format(x))
y = np.random.random((3, 2))
print("\n3x2 array:\n{}".format(y))

# Calculate the dot product of the two arrays
z = np.dot(x, y)
print("\nDot product of two arrays:\n{}".format(z))

print("\n\n-------------- Question 05 --------------\n")

# Calculate yesterday's, today's, and tomorrow's dates
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
print("Yesterday: {}".format(yesterday))
today = np.datetime64('today', 'D')
print("Today: {}".format(today))
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("Tomorrow: {}".format(tomorrow))

print("\n\n-------------- Question 06 --------------\n")

# Generate a random array of 10 values between 0 and 10
x = np.random.uniform(0, 10, 10)
print("Random Array:\n{}".format(x))

# Convert the array to integers using different methods
print("\nMethod 1: {}".format(x.astype(int)))
print("Method 2: {}".format(x - x % 1))
print("Method 3: {}".format(np.ceil(x) - 1))
print("Method 4: {}".format(np.trunc(x)))
print("Method 5: {}".format(np.floor(x)))

print("\n\n-------------- Question 07 --------------\n")
# Define a structured array with 10 elements, each element has two fields: 'position' and 'color'
dtype = [('position', [('x', float, (1,)), ('y', float, (1,))]), 
         ('color', [('r', float, (1,)), ('g', float, (1,)), ('b', float, (1,))])]
x = np.zeros(10, dtype=dtype)

print(x)