m = str(input("do you have any medical conditon(yes/no): "))
if m == "yes":
    a = int(input("Enter your attendence percentage: "))
    if a >= 60:
        print("you are eligable for exam")
    else:
        print("you are not eligable for exam")

elif m == "no":
    a = int(input("Enter your attendence percentage: "))
    if a >= 75:
        print("you are eligable for exam")
    else:
        print("you are not eligable for exam")
else:
    print("invalid output")



