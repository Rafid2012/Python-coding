a = {"Rafid":1,
     "is":1,
     "a student":2}

print("dictoinary: ",a)


value = int(input("Which value you want to check: "))

f = 0

for v in a.values():
    if v == value:
        f+=1

print(f"the frequecy of {value} is {f}")

