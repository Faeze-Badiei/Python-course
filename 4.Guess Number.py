
import random

pc_number=random.randint(0, 100)
print("welcome to the game!")
p=0

while True:
    usernumber=int(input("please enter a number between 0 to 100: "))
    p+=1
    
    if usernumber<pc_number:
        print("enter a bigger number!")   
    if usernumber>pc_number:
        print("enter a smaller number!")
    if usernumber==pc_number:
        print("well done!")  
        break  
    
print(pc_number)
print("number of your guesses: ", p)
