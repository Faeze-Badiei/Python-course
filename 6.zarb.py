m=int(input("Enter the row: "))
n=int(input("Ener the cul: "))

while True:
    for i in range (1,m+1):
        for j in range (1,n+1):
            print(i*j, end=" ")
        print()
    break