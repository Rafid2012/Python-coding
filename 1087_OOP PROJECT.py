class person:
    name = "Rafid"
    occupation = "Python developer"
    networth = 5
    def info(self):
        print(f"{self.name} is a {self.occupation}")
        
a = person()
b = person()

a.name = "Muhammad"
a.occupation = "Artist"

b.name = "Salam"
b.occupation = "Rickshaw puller"
a.info()
b.info()
