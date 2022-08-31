# Ordered collection of elements
# Enclosed in round brackets ()
# Can store different type elements
# Can not change elements once stored (unmutatable)

# creating a tuple
tup1 = ("Million", 10, True, 30.5)
print(tup1)

type(tup1)

# indexing of tuples
# To check the value of 2 index
print(tup1[2])

# To check the value of 1 index
print(tup1[1])

# element count in tuple
len(tup1)

# last element is exclusive (it skips the last element 3 to print all the elem
print(tup1[0:3])

# creating a new tuple
tup2 = (40, "Coders", 9.5, False)
print(tup2)

# concatination of tuples
# merge the elements of tuples
# creating a tupletup1 + tup2

# creating a new tuple
tup3 = (30, 55, 40, 29, 20, 70)
print(tup3)

# to check the minimun value in a tuple
min(tup3)

# to check the maximum value in a tuple
print(max(tup3))

# we can multiply tuples too, but it means repeatation only
# It will repeat the same tuple twice
print(tup3*2)
