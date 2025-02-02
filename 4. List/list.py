# we can create empty list like : list = [0]
# List: A list is a collection of items in a particular order. Lists are mutable, meaning their elements can be changed after they are created. Lists are denoted by square brackets [].
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))
print(len(marks))  #returns length
print(marks[0])

#List can store elements of different types (integer, float, string, etc.)
student = ["Talha", 95.4, 18, "Rawalpindi"]
print(student)

# List are mutable in Python means we can change their data
student[0] = "Faisal"
print(student)

# List Slicing
# Similiar to String Slicing
marks1 = [85, 94, 76, 63, 48]
print(marks1[1:])
print(marks1[-3:-1]) #negative indexing is same as strings


# List Methods
list = [2, 1, 3]
list.append(4) # adds one element at the end, changes the origional list 
print(list)

list.sort() # sorts in ascending order, changes the origional list
print(list)

list.sort(reverse=True) #sorts in descending order
print(list)

fruits = ["banana", "leeche", "apple"]
fruits.sort() # sorts in ascending order, changes the origional list
print(fruits)
fruits.sort(reverse=True) #sorts in descending order
print(fruits)

list.reverse() # reverses the order of elements, changes the origional list
print(list)

list.insert(2, 5) # inserts at specific index, list.insert(index, element)
print(list)

list.remove(1) # removes first occurrence of the element
print(list)

list.pop(3) #removes the element at specific index
print(list)

newlist = list.copy()
print(newlist)


















