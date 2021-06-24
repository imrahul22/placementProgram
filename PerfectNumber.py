#Perfect Number
#Perfect number, a positive integer that is equal to the sum of its proper divisors.
n=int(input("Enter the number"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if n==sum:
    print("%d is a perfect number"%n)
else:
    print("%d is not a perfect number"%n)
