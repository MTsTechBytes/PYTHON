#Set is the collection of the unordered items.
#Set itself is mutable , means it can be changed but 
#Each element in the set must be unique and immutable
#List cannot be added in sets
#Dupilcate values are ignored in Sets
collection = {1, 2, 3, 4, 4}
print(collection)
print(type(collection))
print(len(collection))  #lenght function len() will also don't count duplicate values

#Creating an empty set
collection1 = set()

#Set Methods

print("-------------------------------------------")

#Adding elements to the set
collection1.add(1)
collection1.add(2)
collection1.add("apnacollege")
collection1.add((1, 2, 3))  #passing tuple in set
print(collection1)

#Removing an element from the set
collection1.remove(1)  #if we write collection1.remove(7) it will give error
print(collection1)

#Clearing a set
collection1.clear()
print(len(collection1)) #Ouputs 0

print("-------------------------------------------")

collection2 = {"hello", "apnacollege", "world", "coding", "python"}
print(collection2.pop())  #Picks random values to remove e.g : prints 'hello' or 'coding'

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2))  # Prints union(all the values) of both sets
print(set1.intersection(set2))  # Prints intersection(common value) of both sets