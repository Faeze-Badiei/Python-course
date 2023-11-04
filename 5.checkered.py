F = int(input("Enter a number for one side: "))
B = int(input("Enter a number for aother side: "))

for i in range(F):
    for j in range(B):
        if(i+j)%2==0:
            print("|", end="")
        else:
            print("_", end="")
    print()
