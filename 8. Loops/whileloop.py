# i = 1
# while i <= 5 : 
#     print("Hello")
#     i += 1

#print numbers from 1 to 5 and breaking loop
# i = 1
# while i <= 5 : 
#     print(i)
#     if i == 3 : 
#         break
#     i += 1 

#print a list using loops
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while i < len(nums) : 
#     print(nums[i])
#     i += 1

#search for a number x in tuple using loop
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
while i < len(nums) : 
    if x == nums[i] : 
        print("Found at index:", i)
        break
    else : 
        print("Finding......")
    i += 1

print("-------------------------------")

#Using continue
i = 0
while i <= 5 : 
    if i == 3 : 
        i += 1
        continue
    print(i)
    i += 1

print("-------------------------------")

#Print odd numbers using continue
i = 1
while i <= 10 : 
    if i%2 == 0 : 
        i += 1
        continue
    print(i)
    i += 1



