#Recusrive function to print all values upto n
def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)

show(5)

print("------------------------------------------")

#recursive function for Factorial
def fact(n):
    if (n == 0 or n == 1): #base case
        return 1
    return (n*fact(n-1))


print(fact(3))

print("------------------------------------------")

#Write a recursive function to calculate the sum of the first n natural numbers.
def cal_sum(n):
    if (n == 0):
        return 0
    return (n + cal_sum(n-1))

sum = (cal_sum(5))
print(sum)

print("------------------------------------------")

#Write a recursive function to print all elements in a list
def print_list(list, index = 0):
    if (index == len(list)):
        return 
    print(list[index])
    print_list(list, index+1)

list = [1, 2, 3, 4, 5]
print_list(list)
    