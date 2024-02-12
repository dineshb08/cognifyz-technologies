a=input("Enter the Email: ")
before,after=a.split("@")
domain,address=after.split(".")
if "@" not in a:
    print("Invalid email")
elif any(char in before for char in ['.', '/', '@', '&', '^', '_', '*', '$', '+', '=', '[', ']', ',', '?', '/']):
    print("Invalid Email")
elif len(address)<3:
    print("Invalid Email")
else:
    print("Valid Email")