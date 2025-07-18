u = int(input("Enter the upper number: "))
l = int(input("Enter the lower number: "))

print(f"The power number between {l} and {u} are: ")

for n in range(l,u+1):
    if n > 1:
        for i in range (2, n):
            if (n % i) == 0:
                break
        else:
            print(n,end=" ")