# Write a Python script to sort (ascending and descending) a dictionary by value.

# Example dictionary
my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grapes': 3}

# Sorting in ascending order
ascending_sorted = sorted(my_dict.items(), key=lambda x: x[1])
print("Ascending order:", ascending_sorted)

# Sorting in descending order
descending_sorted = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
print("Descending order:", descending_sorted)
