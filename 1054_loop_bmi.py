while True:
      print("\nWELCOME TO BMI CALCULATOR")

      weight = input("Enter your wieght in Kg or enter 'quit' to exit ").lower()

      if weight == 'quit':
            print('the program was ended')
            break
      
      height = input("Ener your heigh in meter or enter 'quit' to exit").lower()

      if height == 'quit':
            print("the program was ended.")
            break
    
      bmi= float(weight) / float(height) ** 2
      print(bmi,round(2))
