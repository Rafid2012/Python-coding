a = input("Enter the sring you want to check: ")
l = input("Enter the letter you want to check: ")

count = 0

for i in a:
    if i == l:
        count = count + 1
print(f"The letter {l} occurs in the line {a} {count} time")
