a= 10
b = 5
c=15

avg = (a+b+c) / 3

if a < avg:
    print("cyclist 1s speed slower than avarge")
elif b < avg:
    print("cyclist 2s speed slower than avarge")
elif c < avg:
    print("cyclist 3 speed slower than avarge")
elif not (a < avg or b < avg or c < avg):
    print("No one is slower than the average")