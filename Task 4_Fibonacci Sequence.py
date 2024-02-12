def fibo(Term):
    first=0
    second=1
    print(first)
    print(second)
    for i in range(0,Term-2,1):
        temp=first+second
        print(temp)
        first=second
        second=temp

try:
    Term=int(input("Enter the number of terms you want :"))
    fibo(Term)
except ValueError:
    print("Enter the integer Only:")
    