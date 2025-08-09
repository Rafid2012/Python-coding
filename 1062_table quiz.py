while True:
    try:

        n=int(input("enter the index:"))
        for i in range(1,11):
            print(f"{n} * {i} = {n*i}")
    except ValueError as e:
        print(f"Error occured")
         
print("Now answer a quiz: ")

print(f"what is {a} * {a} ?")

print(f"1. {a*3}")
print(f"2. {a*4}")
print(f"3. {a*a}")

c= int(input("Enter your choice: "))

if c== 3:
    print("Correct!")
else:
    print("Incorrect!")
