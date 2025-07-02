h = float(input("Enter your height in metre: "))
w = float(input("Enter your wieght in KG: "))

bmi = w / h**2

if bmi < 18.5:
    print("You are underweight. Gain some weight.")
elif  18.5 <= bmi <= 24.9:
    print("You are normal in weight. keep it up.")
elif 25 <= bmi <= 29.9:
    print("You are overwight. Loose some wight.")
elif 30 <= bmi <= 34.9:
    print("You are obbese. Loosing weigt is emergency for you.")
else:
    print("You are extremely obbese. see a doctor ASAP")