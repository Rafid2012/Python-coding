#capitalize 

txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)

#casefold

txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)


#center
txt = "banana"

x = txt.center(20)

print(x)

#find

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)

#count

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)


#endswith

txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)

#index

txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)


#formst


txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

#title

txt = "Welcome to my world"

x = txt.title()

print(x)
