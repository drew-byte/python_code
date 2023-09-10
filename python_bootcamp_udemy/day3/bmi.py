height = float(input("What is your height: "))
weight = float(input("What is your weight: "))

bmi = round(weight/height**2)
if bmi < 18.5:
   print("Underweight")
elif bmi > 18.5 & bmi < 25:
   print("Normal")
elif bmi > 25 & bmi < 30:
   print("Overweight")
elif bmi > 30 & bmi < 35 : 
   print("Obese")
else : 
   print("Clinically Obese") 