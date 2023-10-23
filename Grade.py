print("Hello!")
n=input("please enter your first name: ")
l=input("and your last name: ")
print("Welcome", n, l)

m=float(input("Now, please enter your math grade: "))
s=float(input("and your science grade: "))
e=float(input("and your english grade: "))
op=float((s+m+e)/3)

if op>=17:
    print("Your average is great. well done!")

if op<17 and op>=12:
    print("Your average is normal. keep trying!")

if op<12:
    print("I'm sorry, you failed.")
