x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if(x > y and x > z):
    print(x, "is greatest in", x, y, z)
elif(y > x and y > z):
    print(y, "is greatest in", x, y, z)
else:
    print(z, "is greatest in", x, y, z)
