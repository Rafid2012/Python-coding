a = [2,4,8,10,12]

s = list(map(lambda x: x**2,a))
print("squared: ",s)

r = list(map(str,a))
print("string: ",r)

q = list(map(lambda x: x+10,a))

print("Added: ",q)

e = list(map(lambda x: x % 2 == 0,a))

print("Is even: ",e)

b = [3,5,7,9]
c = [2,4,6,8]

w = list(map(lambda b,c: b+c,b,c))

print("\nAfter adding: ",w)