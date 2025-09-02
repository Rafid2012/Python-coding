a = (20,40,50,60,78,78,67,60)

a = a + (40,80,70)
print("Extended: ",a)

a = tuple(x for i, x in enumerate(a) if not (x == 20 and i == a.index(20)))
print("after removing: ",a)

if 50 in a:
    ind = a.index(50)
    print(ind)

if 60 in a:
    count_60 = a.count(60)
    print(count_60)

sort = tuple(sorted(a))
print(sort)

rev = tuple(reversed(a))
print(rev)

ld = a[:-1]
wd = a[:-1]

print(f"Before of the last data: {wd} the last data: {ld}")

l = tuple()
print("empty: ",l)