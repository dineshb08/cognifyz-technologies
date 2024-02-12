def converttemp(a,b):
    if a==("celsius"):
        faherheit=(b*9/5)+32
        print("Celsius to Fahrenheit is: ",faherheit)
    elif (a=="fahrenheit"):
        celsius=(b-32)*5/9
        print("Fahrenheit to Celsius is: ",celsius)
    else:
        print("Enter valid measurement")
b=float(input("Enter the temperature: "))
a=input("Enter whether it is celsius or fahrenheit: ").lower()
converttemp(a,b)