from array import array

int_array = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9])

first_elem = int_array[0]
print(first_elem)

# Operations
# Slicing
sliced_arr = int_array[4:8]
print("Sliced Array ", sliced_arr)

# Concatenation - Adding Arrays
t1 = array("i", [1, 2, 3])
t2 = array("i", [4, 5, 6])
t3 = t1 + t2
print("Concat Array", t3)

# Repition - Repeat the same array
t4 = t1 * 3
print("Repition ", t4)


# Array Methods
# append - Add to the end
nums = array("f", [1.00, 1.14, 2.31])
print("Before appending", nums)
nums.append(2.54)
print("After appending", nums)

# extend - Add another array to the end
nums_2 = array("f", [3.14, 4.28])
nums.extend(nums_2)
print("Extended nums", nums)

# insert(pos, val) - Position and Value insertion
nums.insert(0, 1.11111)
print("After insertion", nums)

# remove - remove value if present
nums.remove(1.0)
print("After removing", nums)


# pop - value at positon is removed
nums.pop(0)
print("After popping", nums)
