print("Hello User Welcome to the tip Calculator!")
bill = float(input("Input the bill: "))
tip = int(input("How much tip would you like to give? 10 ,12 , or 15? "))
people = int(input("How many people to split the bill: "))

tip_percent = tip/100
total_tip = bill*tip_percent
total_bill = bill+total_tip
bill_person = total_bill/people
final = round(bill_person,2)
print("The bill is {} and each person should pay {} and the tip is {}".format(bill,final,total_tip))