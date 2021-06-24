#Finding Several leap year in one run
def leap_year(n):

    if n!=0:
        if (n % 400 == 0 or (n % 4 == 0 and n % 100 != 0)):
            print("%d is a leap year" % n)
        else:
            print("%d is not a leap year" % n)
        n = int(input("Enter the year"))
        return leap_year(n)

n=int(input("Enter the year"))
leap_year(n)