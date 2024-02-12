print("Enter Two numbers : ")
a=int(input("Enter first number: "))
b=int(input("Enter Second number :"))
c=input("Enter the Operator :")
if c=="+":
    print("a+b =",a+b)
elif c=="-":
    print("a-b =",a-b)
elif c=="*":
    print("a*b =",a*b)
elif c=="%":
    print("a%b =",a%b)
elif c=="/":
    print("a/b =",a/b)
else:
    print("Enter valid operator")