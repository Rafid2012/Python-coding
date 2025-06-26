a= int(input("Enter your amount: "))

print("denomaition: ")


note1000 = a // 1000
print("1000 taka note: ",note1000)
a= a % 1000

note500 = a // 500
print("500 taka note: ",note500)
a= a % 500

note200 = a // 200
print("200 taka note: ",note200)
a= a % 200

note100 = a // 100
print("100 taka note: ",note100)
a= a % 100



