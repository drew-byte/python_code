#primitive data types
"""
String - "Andrew"
Integer - 21
Float - 50.0
Boolean - True/False
"""

#len command
num_len = len(input("What is your name? "))
print("Your name has {} characters".format(num_len))

#type checking,type conversion & type error
print(type(num_len))

newVersion = str(num_len)
print(type(newVersion))

print(newVersion + 1) #Error because of different data type


