#A built-in data type that let us create immutable sequences of values

#we can also create empty tuple like : tup = ()
#if we want to create a tuple with single value then we would use "comma , " after 1st value like : tup = (1,)
tuple = (2, 1, 3, 1)
print(tuple)
print(type(tuple))
print(tuple[0])
# tuple[1] = 3 is not allowed in tuples

#Tuple Slicing is same as in string and List

#Tuple methods: count(), index()

print(tuple.index(3))  #Output: 2 , returns index of 1st occurence
print(tuple.count(1))  #Output: 2 , counts total occurences 
