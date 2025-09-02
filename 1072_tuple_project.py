a = (6,7,8,9,10,11,12,13)
c = (1,2,5,4,4,8,13,12)
d = tuple(a*c for a,c in zip(a,c))
print(d)
