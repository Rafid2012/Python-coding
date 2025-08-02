def bmicalc(height,weight):
    bmi= weight / height**2
    return bmi

weight = 70
height = 1.34

result = bmicalc(height,weight)

print(f"Result{result}")

