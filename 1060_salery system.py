tax_rate= 0.1

Ss ={
    "CEO": 500,

    "President": 450,

    "Vice President": 400,

    "Manager":300,

    "Assistant Manager":270,

    "Supervisor":230,

    "Team leader":200,

    "Staff":150
}
 
enter={}

def show_Ss():
    print("One hour salary of every employes in their position")
    for position, salary in Ss.items():
        print(f" In positon of {position} salary of hour: {salary} tk.")

def take_enter():
    while True:
        position=input("Enter your position or 'done' to finish: ").strip()

        if position.lower() == "done":
            break

        if position in Ss:
            hour=int(input("Enter how many hours you worked: "))
            if position in enter:
                enter[position] += hour
            else:
                enter[position] = hour
        else:
            print("position doesnt exisist.Please try again")

def cal_earn():
    earn=0.0
    
    for position, hour in enter.items(): 
        earn+=Ss[position]*hour
    tax=earn*tax_rate
    earning_with_tax=earn-tax
    return tax,earning_with_tax
        
def earning():
    print("-----SALARY SUMMERY-----")
    tax,earning_with_tax=cal_earn()
    for position,hour in enter.items():
        print(f"{position} x {hour} = tk.{Ss[position]*hour}")
    print(f"Tax: {tax}")
    print(f"Total SALARY: {earning_with_tax}")

            


if __name__ == "__main__":
    show_Ss()
    take_enter()
    cal_earn()
    earning()