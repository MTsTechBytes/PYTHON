age = 21

if (age >= 18):
    print("Can vote")
    print("Can drive")

light = "green"

if (light == "red"):
    print("Stop")
elif (light == "green"):
    print("Go")
elif (light == "yellow"):
    print("look")
else:
    print("Light is broken")


# Short hand for if else in python
a = 10
b = 20
print("a =", a) if a > b else print("b =", b)