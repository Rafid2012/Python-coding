p = int(input("Enter the price of the product: "))

s = int(input("enter the price you sold: "))

if s > p:
    print("you made profit of",s-p)
else:
    print("you mde loss of",p-s)