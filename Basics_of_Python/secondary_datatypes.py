# Four Collections of Datatypes
def print_type(hd):
    print(type(hd))


# a = list(1, 2, 3, 4, 5)
a = [1, 2, 3, 4, 5]
print_type(a)
print(a[0])
print(a[0] + a[3])

# Property of List - Mutable and Ordered
print("Original Value", a[2])
a[2] = "Hello"
print("Modified Value", a)

b = (1, 2, "Hello", 4, 5)
print_type(b)
print(b[2])
print(b[0] + b[1] + b[4])

# Property of Tuple - immutable and Ordered
print("Original Value", b[2])
try:
    b[2] = "Hello"
    print("Modified Value", b)
except Exception:
    print("Ayyayoo, error")

# Set - Unordered and No repetition and Mutable
muki = {"Martin", "David Fincher", "David Fincher", "Miskin"}
sandy = {"Mari Selvaraj", "GVM", "David Fincher", "Miskin"}

# Intersection and Union
# Intersection - and
# Union - Or
print(sandy.union(muki))
print(muki.union(sandy))
print(sandy.intersection(muki))
print(muki.intersection(sandy))

muki.add("Chris")
print(muki)

# Discard and Remove
sandy.discard("GPM")
print(sandy)


chocolate = {"Silk": 100, "Kitkat": 50, "Temptations": 100}

print(chocolate["Silk"])

chocolate["Silk"] = chocolate["Silk"] + 10
print(chocolate["Silk"])

chocolate["Kitkat"] = 60
print(chocolate["Kitkat"])
