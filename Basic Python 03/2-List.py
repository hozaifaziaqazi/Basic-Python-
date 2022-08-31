# Ordered collection of elements
# Enclosed in sqaure brackets [ ]
# Can change values (mutatable)

# creating a list
list1 = [5, "Million", False]
print(list1)

type(list1)

# length of List
len(list1)

# indexing of list
# to print the value of index 1
print(list1[1])

# creating a new list
list2 = [15, "Coders", True, 30.4]
print(list2)

# concatination of List
# merge the elements of lists
print(list1 + list2)

# we can multiply lists too, but it means repeatation only
# It will repeat the same list twice
print(list1*2)

# To reverse the list elements
print(list1.reverse())
print(list1)

# To append any word or character with list
print(list1.append("Python Programming"))
print(list1)

# To count the occurance of specific list element
list1.count("Python Programming")

# creating a new list
list3 = [30, 10, 4, 33, 55, 78, 89, 60, 90]
print(list3)

print(len(list3))


# Sorting a list (To arrange in ascending orders)
print(list3.sort())
print(list3)
