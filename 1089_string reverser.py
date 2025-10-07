class SR:
    def __init__(self,string):
        self.string = string
    def RS(self):
        return self.string[::-1]
    
a = SR("Hello world")
rt = a.RS()
print(f"Main string: {a.string}")
print(f"Reversed string: {rt}")
