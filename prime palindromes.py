a=int(input("Enter a number: "))
if a>1:
    for i in range(2,a):
        if (a%i)==0:
            print("not a prime number")
            break
    else:
        print("a prime number")
        x=a
        rev=0
        while a>0:
            rev=(rev*10)+a%10
            a=a//10
        if x==rev:
            print("a palindrome number")
        else:
            print("not a palindome number")
else:
    print("not a prime number")
    