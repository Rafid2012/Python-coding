while True:
    try:
        a = int(input("Enter your age: "))
    except ValueError as v:
        print(f"Error occured {v}")
        continue

    if a % 2 == 0:
        print("your is even.")
    else:
        print("your age is odd")




