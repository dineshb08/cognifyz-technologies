def Palindrome(a):
    b=""
    for i in range(len(a)-1,-1,-1):
        b+=a[i]
    if a==b:
        print("it's a Palindrome")
    else:
        print("Not a Palindrome")
a=input("Enter a String :").lower()
Palindrome(a)
