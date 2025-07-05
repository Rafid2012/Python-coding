c = int(input("enter the unit of electricity consumed:  "))

if c < 50:
    bill = c * 2.60
    tax = 25
elif c <= 100:
    bill = (50*2.60) + ((c - 50) * 3.25)
    tax = 35
elif c <= 200:
    bill = (50*2.60) + (50*3.25) + ((c - 100) * 5.26)
    tax = 45
else:
    bill = (50*2.60) + (50*3.25) + ((c-200) * 8.45)
    tax = 75

total = bill + tax
print(f"You have to pay {total}")
