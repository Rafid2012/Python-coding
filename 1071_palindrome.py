a = input("enter the tuple elements seperated by coma: ")

b = a.split(",")

c = tuple(b)

if c == c[::-1]:
    print("the elements are palindrome")
else:
    print("the elements are not palindrome")