a=int(input("Enter a number for first side: "))
b=int(input("Enter a number for second side: "))
c=int(input("Enter a number for third side: "))

if a+c>b and b+c>a and a+b>c:
    print("You can draw a triangle with these numbers.")
else:
    print("There isn't any triangle with these numbers.")
