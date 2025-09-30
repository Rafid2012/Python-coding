class employee:
    def __init__(self,emp_id,name,hourly_rate):
        self.emp_id=emp_id
        self.name=name
        self.hourly_rate=hourly_rate
        self.hourly_work=0

    def set_work_hour(self,hour):
        self.hourly_work = hour

    def calculate_salary(self):
        self.hourly_rate*self.hourly_work

    def info(self):
        print(f"Employee's ID: {self.emp_id}")
        print(f"Employees's name: {self.name}")
        print(f"Type: {self.employee_type()}")
        print(f"Hours worked: {self.hourly_work}")
        print(f"Hourly rate: {self.hourly_rate} TAKA")
        print(f"Salary: {self.calculate_salary()} TAKA ")

    def employee_type(self):
        return "General employee"
    
class regularemployee(employee):
    def calculate_salary(self):
        base_salary = super().calculate_salary()
        if self.hourly_work > 160:
            bonus = 0.10*base_salary
            return base_salary + bonus
        return base_salary
    def calculate_overtime_bonus(self):
        if self.hourly_work > 160:
            bonus = 0.10 * (self.hourly_work*self.hourly_rate)
            print(f"[NOTE] overtime bonus {bonus:.2f} TAKA ")
        else:
            print(["Note] no overtime bonus"])

    def employee_type(self):
        return "regular employee"
    
class temporaryemployee(employee):
    def check_max_hours(self):
        if self.hourly_work > 120:
            print("[Warning] temporary worker excceded 120 hours ")
            print()
        else:
            print("Temporary employee didnt excceced the work limit")
    def employee_type(self):
        return "temporary employee"
    

if __name__ == "__main__":
    emp1 = regularemployee(emp_id=301,name="Rahim hasan",hourly_rate=120)
    emp2 = temporaryemployee(emp_id=902,name="karim hoque",hourly_rate=60)
    emp3= regularemployee(emp_id=345,name="shafiqul islsm",hourly_rate=120)
    
    emp1.set_work_hour(120)
    emp2.set_work_hour(80)
    emp3.set_work_hour(125)
    employees = [emp1,emp2,emp3]
    for emp in employees:
        emp.info()
        if isinstance(emp,regularemployee):
            emp.calculate_overtime_bonus()
            print()
        elif isinstance(emp,temporaryemployee):
            emp.check_max_hours()


    

    
        
     
    

    