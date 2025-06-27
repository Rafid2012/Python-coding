a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
c = int(input("enter your third number: "))

if a > b and a > c:
    print("a is bigger")
elif b > a and b>c:
    print("b is bigger")
else:
    print("c is bigger")