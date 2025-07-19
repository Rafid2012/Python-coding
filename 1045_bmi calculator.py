w = float(input("Enter your weight in KG: "))
h = float(input("Enter your weight in height in meter: "))

bmi = w / h**2
print(f"your bmi is: {bmi:0.2f} ")

if bmi < 18.5:
    print("You are underweight. Gain some weight")

elif 18.5 <= bmi <= 24.9:
    print("You are normal. keep it up.")

elif 25 <= bmi <= 29.9 :
    print("You are overweight. loose some weight")

elif 30 <=  bmi <= 34.9:
    print("You are obbese. loose some weight imedietly")

else:
    print("You are extremely obbese. visit the doctor ASAP")