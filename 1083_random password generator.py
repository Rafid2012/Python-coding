import random

chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@!#$%()"

password=""
l = int(input("enter length: "))
for i in range(l):
    password+=random.choice(chars)
print(password)