class student:
    def __init__(self,name,age):
      self.name = name
      self.age = age

    def getinfo(self):
        print(f"My name is {self.name} and my age is {self.age} ")

a = student("Rafiq",16)
a.getinfo()