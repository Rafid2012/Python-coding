num = int(input("enter the number: "))
digits = [int(d) for d in str(abs(num))]

n = len(digits)

if n == 0:
    print("No middle number exists")

if n%2 == 1:
    result = digits[n // 2]
else:
    mid1 = digits[n // 2-1]
    mid2 = digits[n // 2]
    result = mid1 * mid2

print(f"midproduct of {num} is {result}")