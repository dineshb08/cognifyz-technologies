#string reversal program
def reverse(a):
    b=""
    for i in range(len(a)-1,-1,-1):
        b+=a[i]
    return b
a=input("Enter a String: ")
print(reverse(a))