veggies = ["potatoes", "brinjal", "ladyfinger", "cucumber"]
for val in veggies : 
    print(val)

print("-----------------------------------------------")

tup = (1, 2, 3, 4, 5)
for val in tup : 
    print(val)

print("-----------------------------------------------")

#We can also use else with for loop, else is used for those task which we want to execute in the end of the loop
str = "apnacollege"
for char in str : 
    if char == 'o' :
        print("o found")
        break
    print(char)
else :              #else case will not execute when there is break, it will only execute when the loop runs till end
    print("END")

print("-----------------------------------------------")

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for el in nums : 
    print(el)

print("-----------------------------------------------")

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49
index = 0
for el in nums :
    if x == el :
        print("number found at index:", index)
    index += 1

print("-----------------------------------------------")
print("-----------------------------------------------")

#Using RANGE in for loop
     #optional, compulsory, optional
#range(start?,    stop,     step(gap)?)
#if only starting and stopping value is given then by default it increments by 1
#if only stopping value is given then it will start from 0 to that stopping value and increments by 1

#seq = range(5)
#print(seq[0]) , we are accessing indexes
#OR by for loop
#for i in seq : 
#    print(i)

#WHOLE ABOVE CODE CAN BE WRITTEN AS:

for a in range(5) : #5 will not be printed, only 0 - 4 will print
    print(a)

print("-----------------------------------------------")

num = 10
for b in range(2, num) : #range(start, stop)
    print(b)

print("-----------------------------------------------")

for c in range(2, 10, 2) : #range(start, stop, step(gap))
    print(c)

print("-----------------------------------------------")

#We can also print in reverse in range
for d in range(100, 0, -1) :
    print(d)

print("-----------------------------------------------")

#printing table using range() function
n = int(input("Enter a number: "))
for e in range(1, 11) :
    print(n*e)

print("-----------------------------------------------")

#Pass Statement
#pass is a null statement that does nothing. It is used as a placeholder for future code
for f in range(5) : 
    pass 
i = 4
if i > 5:
    pass


