#nested if cindition
a=int(input("enter value of a"))
b=1000
print("the sum is",a+b)
if(a+b>=0):
    print("the no is positive")
    if (a+b<=1005):
        print("the no is small")
    else:
        print("the no is large")

else:
    print ("the no is negative")
