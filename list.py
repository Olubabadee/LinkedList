# Create an empty list called my_list.
# Append the following elements to my_list: 10, 20, 30, 40.
# Insert the value 15 at the second position in the list.
# Extend my_list with another list: [50, 60, 70].
# Remove the last element from my_list.
# Sort my_list in ascending order.
# Find and print the index of the value 30 in my_list.

# Create List 
my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

# Insert 15
my_list.insert(2, 15)

print(my_list)

list2 = [50, 60, 70]

# Extend List
my_list.extend(list2)

print(my_list)

# Sort List
my_list.sort()

print(my_list)

# Find Index
print(my_list.index(30))