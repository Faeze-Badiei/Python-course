
import math

print("welcom!")
while True:
    s=input("And choose one of (+, -, *, /, sin, cos, tan, cot, factorial, sqrt, exit):")
    if s=="exit":
        break
    
    n=int(input("Now enter a number:"))

if s=="sin":
    r=(math.sin(math.radians(n)))

if s=="cos":
    r=(math.cos(math.radians(n)))

if s=="tan":
    r=(math.tan(math.radians(n)))

if s=="cot":
    z=(math.tan(math.radians(n)))
    r=1/z

if s=="sqrt":
    r=(math.sqrt(n))

if s=="factorial":
    r=(math.factorial(n))

if s=="+":
    a=float(input("please enter another number:")) 
    r=n+a

if s == "-":
    b=float(input("please enter another number:"))
    r=n-b

if s=="*":
    c=float(input("please enter another number:")) 
    r=n*c

if s == "/": 
    d=float(input("please enter another number:"))
    if d==0:
        r="Error! plaese try with another number"
    else:
        r=n/d

print(r)
