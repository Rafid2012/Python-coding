a = int(input("Enter the year you want to cheack: "))

if a % 400 == 0:
    print(a,"is a leap year")
elif a % 100 == 0:
    print(a,"It is not a leap year")
elif a % 4 == 0:
    print(a,"is a leap year")
else:
    print(a,"Not a leap year")