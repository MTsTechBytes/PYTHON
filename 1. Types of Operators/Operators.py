#Arithmetic Operators
a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)  # Answer Always comes in float like 2.0
print(a % b)  
print(a ** b) #Power operator(a ** b means a raise to power b, or a^b)  


# Relational/Comparison Operators
c = 50
d = 20

print(c == d)  #False
print(c != d)  #True
print(c >= d)  #True
print(c > d)  #True
print(c <= d)  #False
print(c < d)  #False


# Assignment Operators
num1 = 10 
num1 += 10
print("num1 :", num1)

num2 = 20
num2 -= 10
print("num2 :", num2)

num3 = 3
num3 *= 2
print("num3 :", num3)

num4 = 50
num4 /= 10
print("num4 :", num4)

num5 = 5
num5 %= 2
print("num5 :", num5)

num6 = 10
num6 **= 5
print("num6 :", num6)


# Logical Operators
x = 50
y = 30
print(not False)
print(not (x > y))  #False

val1 = True
val2 = False
print("AND operator:", val1 and val2) #False
print("OR operator:", (x == b) or (x > b))  #True