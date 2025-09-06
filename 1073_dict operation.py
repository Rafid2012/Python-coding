a = {
    "1": {"Name" : "Rashid","Age" : 13,"Gender" : "Male"},
    "2": {"Name" : "Niaj","Age" : 13,"Gender": "male"},
    "3": {"Name" : "Nisha","Age" : 43,"Gender": "Female"}

}

# Access

print("accessing a studint", a["1"])
print("Accessing student by get", a.get("2"))

# add
a["4"] = {"Name" : "Fahim","Age" : 15,"gender" : "male"}
print("\nafter adding ",a)

# update
a["2"]["Name"]= "Niaj Hasan"
print("\nafter update", a)

# remove

r = a.pop("4")
print("\n after pop ",r,"\nafter pop:",a)


print("\nkeys: ",a.keys())
print("values:",a.values())
print("items: ",a.items())


