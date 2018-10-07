print("a is addition",)
print("s is subtraction")
print("d is division")
print("m is multiplication")
x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
opt=input("enter an option:")
if(opt=='a'):
    print("x+y=",x+y)
elif(opt=='s'):
    print("x-y=",x-y)
elif(opt=='d'):
     print("x/y=",x/y)
elif(opt=='m'):
     print("x*y=",x*y)
else:
     print("Invalid option")
