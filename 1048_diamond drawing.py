a = int(input("enter the number of row you want: "))

if a % 2 == 0:
    half = a // 2
else:
    half = a // 2 + 1

space = half-1

for i in range(1,half+1):
    print(" " * space + "*" * (2 * i - 1))
    space -= 1

space = 1

for i in range(half-1,0,-1):
    print(" " * space + "*" * (2 * i - 1))
    space += 1

