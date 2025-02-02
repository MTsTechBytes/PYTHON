# str1 = "This is a string"
# str2 = 'ApnaCollege'
# str3 = """This is also a string"""

str1 = "This is a string.\nWe are creating it in python." #escape sequences are also counted as character(\n is single character)
print(str1);
print(len(str1));

str2 = "Hello"
str3 = "World"
print(str2 + str3)
print(str2[0])
#str2[1] = "a" this is wrong we cannot change any character in string like this


#Slicing string
str4 = "Python is awesome"
# str4[starting_index : ending_index] #ending index is not included
print(str4[0:6]) #prints "Python"
print(str4[7:]) #prints "is awesome" #strr4[7:] means strr4[7:to end]
print(str4[:6]) #prints "Python"     #strr4[:6] means strr4[0:6]


# A  p  p  l  e
#-5 -4 -3 -2 -1
str5 = "Apple"
print(str5[-5:]) #prints "Apple"

#More String Functions
str = "i am a coder."
print(str.endswith("er.")) #returns True if string ends with substring

print(str.capitalize()) #Capitalizes 1st character # does not changes the origional string, works only when used

print(str.replace("o", "a")) #Replaces all o's with a's, but don't changes the original string.
print(str.replace("coder", "programmer")) 

print(str.find("o")) #returns 1st index of 1st occurrence #8
print(str.find("am"))
print(str.find("l")) #returns -1 because l doesn't exist 

print(str.count("a")) #returns 2 #number of times "a" is present in the string
print(str.count("i"))
