# side1= int(input("Enter length of 1st side: "))
# side2= int(input("Enter length of 2nd side: "))
# side3= int(input("Enter length of 3rd side: "))
# if (side1 == side2 == side3):
#     print("Equilateral")
# elif ((side1 == side2)and(not side2 == side3)):
#     print("Isosceles")
# else:
#     print("Scalene")

flat_rate = 50
additional_rate = 10 
fare = None

distance = float(input("Enter the distance travelled (in km): "))
if distance > 0:
    if distance <= 1:
        fare = flat_rate
    else:
        fare = flat_rate + (distance-1) * additional_rate

    print("The total fare is =", fare)
