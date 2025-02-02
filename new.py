# Initializing variable
number = 2

#Printing Variable
print(number)

#Assigning same value to multiple values
a = b = c = 3
print(a, " ", b, " ", c)

#Assinging multiple values to multiple varibles
x, y, z = 1, 2, 3
print(x , y , z)

u, v, w = "Orange", "Banana", "Cherry"
print(u, v, w)

#Initializing variable with no value, so we use None to keep it empty
name = None
print(name)

#Taking input in 
name = input("What is your name: ")
print("Your name is: " + name)
# When we take input in python the compiler automatically converts the type of input into string even though we entered a number, like if we enter 2 it wil be converted to string while input, so we use typecasting at the time of input to get the appropriate results
val = int(input("Enter a decimal number"))
print("val = ", val)

"""Determining the type of variable
Typecasting (from number to string)"""
num = 7 
print(type(num))

word = str(num)
print(type(word))

#Typecasting (from string to number)
str = '3'  
num = int(str)
print(num , "is" , type(num))

#Difference between , and +
name1 = "Talha"
name2 = 'Faisal'
print("By using ," , name1 , name2)
print("By using +" , name1 + name2)


#Unpacking
fruits = ["apple", "banana", "cherry"]
f1, f2, f3 = fruits
print(f1, f2, f3)

#Concatenating int with string
m = 5
n = "John"
print(m + n)

#Declaring and Defining function 
def fun():
    global x 
    x = "language"
    print("Python is " + x)

fun() #function invoking/calling
print("Python outside the function " + x )

#Using Shorthand for if else
num1 = input("Enter a number: ")
print(num1 , "is positive") if num1>0 else print(num1 , "is negative")

#Using if , elif(else if) , else
x = input("Enter first numbers: ")
y = input("Enter second numbers: ")

if x>y :
    print(x , "is greater than", y)

elif x<y:
  print(x , "is smaller than", y)

else :
   print(x , " = ", y)



    




