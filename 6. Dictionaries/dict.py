#Dictionaries are used to store data values in key:value pairs
#They are unordered, mutable(changeable) and don't allow to create duplicate keys

#Creating an empty dictionary

empty_dict = {}
print(empty_dict)
print(type(empty_dict))

#Creating a dictionary
info = {
    "Name": "John",
    "Age": 30,
    "City": "New York",
    "Subjects": ["python", "C", "Java"],
    "Topics": ("dict", "set"),
}

print(info)
print(type(info))

print("-------------------------------------------")

#Accessing Keys in Dictionaries
print(info["Name"])  #Prints John

print("-------------------------------------------")

#Updating values in Dictionaries
info["Name"] = "Kevin"
print(info["Name"])  #Prints Kevin

print("-------------------------------------------")

#Adding new key-value pairs
info["SurName"] = "Hart"  # new key-value pair will be added at the end
print(info["SurName"])
print(info)

print("-------------------------------------------")

#Deleting key-value pairs
del info["Age"]
print(info)

print("-------------------------------------------")

# Nested Dictionaries
student = {
    "name": "Alice",
    "subjects" : {
        "phy" : 97,
        "chem" : 88,
        "math" : 95
    },
}
print(student)
print(student["subjects"])
print(student["subjects"]["phy"])  # Prints 97

print("-------------------------------------------")

# Dictionary methods
print(student.keys())    #returns all keys
print("-------------------------------------------")
print(student.values())  #returns all values
print("-------------------------------------------")
print(student.items())   #returns all key-value pairs
print("-------------------------------------------")
print(student.get("name")) #ouputs same as print(student["name"]) but it will not will give error when we type the key name wrong, rather than that it will ouput None
student.update({"age": 18}) #outputs same as student["age"] = 18 insert the specified items to the dictionary
print("-------------------------------------------")
print(student) #new key value will be also shown