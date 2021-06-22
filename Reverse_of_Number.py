#Reverse of a nunber
n=int(input("Enter a Number"))
def reverse(n):
    rev=0
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    print(rev)
reverse(n)

print()



def Reverse(n):
    global Times
    if(n > 0):
        print(n % 10, end="")
        Reverse(n // 10)
Reverse(n)



