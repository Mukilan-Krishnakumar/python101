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
