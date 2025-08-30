a = [20,23,66,69,55,78,38,20,23,56,23,40]
# Append
a.append(30)
print("Append: ",a)
# Extend 
a.extend([300,500,788,678])
print("extended: ",a)

# Insert
a.insert(3, 77)
print("Inserted: ",a)

#remove
for n in a:
    if n == 23:
        a.remove(23)
print("removed", a)

#pop
popped=a.pop()
print("popped",a,popped)

#count
counted = a.count(20)
print("count : ",a,counted)

#index
if 69 in a:
    i = a.index(69)
    print(a, "Index of 69 is: ",i)



