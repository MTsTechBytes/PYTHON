#Q1
cities = ["Rawaloindi", "Islamabad", "Karachi", "Lahore", "Quetta", "Peshawar"]
heroes = ["Batman", "Superman", "Spiderman", "Aquaman"]

def print_len(list) : 
    print(len(list))
    
print_len(cities)
print_len(heroes)

print("------------------------------------")

#Q2
def print_list_elements(list) : 
    for item in list :
        print(item, end = " ")

print_list_elements(cities)
print()
print_list_elements(heroes)

print("------------------------------------")

#Q3
def find_fact(n) :
    fact = 1
    for i in range(1, n+1) : 
        fact *= i
    print("Factorial =", fact)

find_fact(5) 

print("------------------------------------")

#Q4
def USD_to_PKR(usd) :
    pkr = usd * 280
    print(usd, "USD =", pkr, "PKR")

USD_to_PKR(100)

print("------------------------------------")

#Q5
def Even_or_Odd() :
    num = int(input("Enter a number: "))
    if num%2 == 0 : 
        return "EVEN"
    else :
        return "ODD"
    
print(Even_or_Odd())
print(Even_or_Odd())
