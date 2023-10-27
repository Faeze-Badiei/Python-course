import random

while True:
    R = input("roll or exit:")
    if R == "exit":
        break
    if R == "roll":
        d=random.randint(1,6)
        print(d)
        if d==6:
            d=random.randint(1,6)
            print(d)
    break
