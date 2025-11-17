import random
'''
n1 = int(input("Enter a number \n"))
if n1 >= 1:
    print("Number between 1-100")
elif n1 <= 100:
    print("Number between 1-100")
else:
    print("Number not between 1-100")

name = input("Enter name: ").upper()
age = int(input("Enter age: "))
tscorelimit = int(input("Enter the maximum score: "))
tscore = int(input("Enter your test score: "))
if tscore >= tscorelimit/4:
    passed = True
else:
    passed = False


final = f"Name:  {name}\nAge:  {age}\nTest score: {tscore}/{tscorelimit}\nPassed?: {passed}"
print(final)
'''
ctemp = int(input("Enter the temperature (°C): "))
ftemp = (ctemp*9/5)+32
print(f"{ctemp}°C is {ftemp}°F")