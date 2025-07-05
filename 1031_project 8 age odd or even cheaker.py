age = int(input("Enter your age: "))

if age >= 18:
    if age % 2 == 0:
        print(f"your age {age} is even")
    else:
        print(f"your age {age} is odd")
else:
    print("You are under age")
