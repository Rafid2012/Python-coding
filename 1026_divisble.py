n = int(input(("Enter the number you want to cheack: ")))
d = int(input(("Enter the divisior: ")))

if d == 0:
    print("0 is not allowed as a divisior")
elif n % d == 0:
    print(f"{n} is divisble by the number {d}")
else:
    print(f"{n} is not divisble by the number {d}")