#GCD & LCM of two number

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
i = 1
while(i <= num1 and i <= num2):
  if(num1 % i == 0 and num2 % i == 0):
    gcd = i
  i = i + 1
print("GCD is", gcd)
lcm=(num1*num2)//gcd
print("LCM is",lcm)


#GCD of more than two no in a array

def findgcd(x, y):
  while (y):  #means{while(y!=0)}
    x, y = y, x % y
  return x


l = [22, 44, 66, 88, 99]
num1 = l[0]
num2 = l[1]
gcd = findgcd(num1, num2)
for i in range(2, len(l)):
  gcd = findgcd(gcd, l[i])
print("gcd is: ", gcd)



#prog2
def findgcd(x, y):
  if y == 0:
    return x
  else:
    return findgcd(y, x % y)


l = [22, 44, 66, 88, 99]
num1 = l[0]
num2 = l[1]
gcd = findgcd(num1, num2)
for i in range(2, len(l)):
  gcd = findgcd(gcd, l[i])
print("gcd is: ", gcd)