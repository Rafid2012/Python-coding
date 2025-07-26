a = int(input("Enter the how many rows you want: "))
 
for i in range(a+1):
    for j in range (i + 1):
        print("*", end="")
    print()

for i in range (a-1,-1,-1):
    for j in range(i+1):
        print("*",end="")
    print()

        
    


