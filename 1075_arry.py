import array

a = array.array("i",[1,2,3,4,5,6])

a.append(2)
print("appned: ",a)

a.insert(4,69)
print("after insert: ",a)

a.remove(6)
print("after remove: ",a)

a.pop()
print("after pop: ",a)