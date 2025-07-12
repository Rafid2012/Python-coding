running = True

while running:
    a = int(input("Enter the number: "))
    if a %2 == 0:
        print(f"{a} is a even number")
    else:
        print(f"{a} is a odd number")
        running = False