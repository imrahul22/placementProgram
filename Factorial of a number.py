#Factorial of a number

def fact(n):
    while n==0:
         return 1
    while n!=0:
        return n*fact(n-1)


n=int(input("Enter the number"))
print(fact(n))
