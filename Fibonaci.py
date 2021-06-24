#Fibonaci SEries
n=int(input("How many number you want in the series"))
a=0
b=1
print(a)
print(b)
while n-2>0:
    c=a+b
    print(c)
    a=b
    b=c
    n=n-1
