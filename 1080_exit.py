while True:
    a = input("Enter a number or type 'quit' to exit: ")
    if a.lower() == "quit":
        exit()
    n = int(a)
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")