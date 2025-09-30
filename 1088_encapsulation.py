class student:
    def __init__(self,grade,name):
        self.__grade = grade
        self.name = name 

    def get_grade(self):
        return self.__grade
    
    def set_grade(self,grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade")

s = student("Rahim",6)
print(s.name,s.get_grade())
s.set_grade(12)
print(s.name,s.get_grade())