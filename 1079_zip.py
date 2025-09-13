a = [2,4,8,7]
b = ["a","b","c"]
t = {4,8,10,12}

c = list(zip(a,b))
print("after zipping: ",c)

d = list(zip(a,t))
print("after zipping a,t: ",d)

for x,y in zip(a,b[::-1]):
    print(x,y)

s = ["relianse","apple"]
p = [234,456]

e = {s:p for s,
     p in zip(s,p)}
print(e)

