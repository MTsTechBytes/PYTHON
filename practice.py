#Reversing a string
# string = input("Enter a string: ")
# print("The original string is: ", string)

# reversedstring = string[::-1]
# print("The reversed string is: ", reversedstring)

print("-------------------------------------------------------------")

# pul=input("enter a string:" )
# def func(abc):
#    reverse_words=abc[::-1]
#    for var in reverse_words:
#     print (var)
# (func(pul))

print("-------------------------------------------------------------")

# pul=input("enter a string:" )
# def func(abc):
#    reverse_words=abc[::-1]
   
#    return (reverse_words)
# print(func(pul))

print("-------------------------------------------------------------")

#write a recursive function to reverse a string
# def reverse_string(string):
#     if len(string) == 0:
#         return string
#     return reverse_string(string[1:]) + string[0]

# print(reverse_string("hello"))

print("-------------------------------------------------------------")

#Write a program to find the sum and average of all elements in a list.
# list = [2, 44, 23, 13 ,42]
# s = 0
# for i in list:
#     s = s + i

# print(s) 
# numbers = sum(list)
# print(numbers)

print("-------------------------------------------------------------")

#Write a program to find the second largest element in a list.
# list = [42, 53, 21, 64, 75]

# Given the list [10, 20, 30, 40, 50], find the maximum and minimum elements by using function
# list = [10, 20, 30, 40, 50]
# maximum = max(list)
# print(maximum)
# minimum = min(list)
# print(minimum)

print("-------------------------------------------------------------")

#Taking input in list
# list = []
# n = int(input("Enter the range of the list"))
# for i in range(n):
#     element = int(input(f"Enter element {i+1}:"))
#     list.append(element)

# print(list)

# print("A is greates") if 10>5 else print("B is largest")

# for i in range(0, 12, 2):
#     print(i, end=" ")
#     if i == 6:
#         break
# else:
#     print("END")

print("-------------------------------------------------------------")

# Create a function that takes a number as input and returns its square.
# def square(n):
#     return n*n

# x = square(int(input("Enter a number : ")))
# print(x)

print("-------------------------------------------------------------")

#Define a function that converts Celsius to Fahrenheit.
# def Cal_to_Fah(c):
#     f = (9/5)*c + 32
#     return f

# celsius = float(input("Enter temperature in Celsius: "))
# print(Cal_to_Fah(celsius))

print("-------------------------------------------------------------")

#Define a function that counts the number of vowels in a given string.

def countVow(str):
    global count
    count = 0
    vowel = "AEIOUaeiou"
    for val in str:
        if val in vowel:
            count += 1
    return count

string = input("Enter a string : ")
print(countVow(string))
print("There are ", count , "Vowels")


    