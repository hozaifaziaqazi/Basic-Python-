# Un-Ordered collection of elements
# Enclosed in curly brackets {}
# Store Key and value
# Can change values (mutatable)

# creating a dictionary
dict1 = {"mac":100000, "dell":70000, "hp":60000, "lenovo":50000}
print(dict1)

# To check the type
print(type(dict1))

# Extract data
# Extracting keys (show only keys of dictionary)
print(dict1.keys())

# Extracting values (show only values of dictionary)
print(dict1.values())

# adding new element
dict1["acer"] = 40000
print(dict1)

# update the value of mac
dict1["mac"]=120000
print(dict1)

# create a new dictionary
dict2 = {"mouse":300, "keyboard":400, "headphone":1000}
print(dict2)

# concatinate dic1 with dict2
# need to use update to concatenate
dict1.update(dict2)
print(dict1)

