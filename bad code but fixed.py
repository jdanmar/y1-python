def hospital():
    Name = input("Enter Patient Name: ")
    Height = float(input("Height (m): "))
    Weight = float(input("Weight (kg): "))
    bmi= float(Weight)/(float(Height)*float(Height))
    if bmi > 30:
        print("Overweight")
    else:
        print("Balanced Weight")
    print("Patient:",Name,"has bmi of",bmi)
hospital()

'''
Original:
def hospital():
    NME=input("enter Patient Name:")
    Age =input("AGE:")
    height= input("height")
    weight= input("WEIGHT")
    bmi= float(weight)/(float(height)*float(height))
    if bmi>30:print("overweight")
    else:print("ok")
    if Age>65:print("Old person discount applied")
    print("Patient:",NME,"has bmi of",bmi)
hospital()

No indents for else and if
Variables are all over the place
Old person discount shouldn't be in the same function as a BMI calculator
Variable input values aren't specified - python will try to guess them but get it wrong
Certain strings arent capitalised
Age isn't required
NME shouldn't be a constant
'''