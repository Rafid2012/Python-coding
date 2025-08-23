import datetime
import calendar

def menu():
    print("\n Date, Time and Calendar Utility ")
    print("1.Show todays date")
    print("2.Show current time in Dhaka")
    print("3.Show weekdays")
    print("4.Show calendar of a month")
    print("5.Days between two dates")

def todays_date():
    t=datetime.date.today()
    print(t)
def comaparing_time():
    d1=int(input("Enter the first date (YYYY-MM-DD)"))
    d2=int(input("Enter the second date (YYYY-MM-DD)"))
    try:
        date1=datetime.datetime.strptime(d1,"Y%-m%-d%")
        date2=datetime.datetime.strptime(d2,"Y%-m%-d%")
        c = abs((date2-date1).days)
        print(f"Days between: {c}")
    except ValueError:
        print("invalid enter")

def show_wd():
    try:
        e = int(input("Enter the date (YYYY-MM-DD)"))
        r = datetime.datetime.strptime(e,"Y%-m%-d%").date()
        print(f"{e} is a {r.strftime('%A')}")
    except ValueError:
        print("Invalid enter")

def show_Mcalander():
    try:
        y=int(input("Enter a year (e.g 2025): "))
        m = int(input("Enter a month (1-12): "))
        print(calendar.month(y,m))
    except Exception:
        print("Invalid input")

def show_time():
    
        now=datetime.datetime.utcnow() + datetime.timedelta(hour=6)
        print("current time in dhaka.", now)
    
def main():
    while True:
            menu()
            a=int(input("Enter choice: (1-6): "))
            if a == 1:
                 todays_date()
            if a == 2:
                 show_time()
            if a == 3:
                show_wd()
            if a == 4:
                show_Mcalander()
            if a == 5:
                 comaparing_time()

if __name__=="__main__":
        main()




