from rich import print # here to change the text colour (pip install colorama in the terminal)
valid = True
steps = 0
calories = 0
def DDC():
    recommended = int(input("Enter the recommended dose (mg): "))
    kgweight = int(input("Enter your weight (kg): "))
    maxdailydosage = recommended*kgweight
    print(f"Your Maximum Daily Dosage: {maxdailydosage} mg/d")
    menureturn = input("Would you like to return to the Healthcare Helper? Y/N\n")
    if menureturn.lower() == "y":
        valid = True
        HCHelper()
    else:
        print("Goodbye!")
        exit()
def BMICALC():
    patientWeight = int(input("Enter your weight (kg): "))
    patientHeight = int(input("Enter your height (cm): "))
    metreheight = patientHeight/100
    bmi = round(patientWeight/metreheight**2,1)
    if bmi <= 18.5:
        bmicategory = "Underweight"
    elif bmi <= 24.9:
        bmicategory = "Normal weight range"
    elif bmi <= 29.9:
        bmicategory = "Class 1 Obesity"
    elif bmi <= 39.9:
        bmicategory = "Class 2 Obesity"
    elif bmi <= 40:
        bmicategory = "Class 3 Obesity"
    else:
        print("Invalid numbers")
        BMICALC()
    print("BMI: ",bmi)
    print("BMI Category: ",bmicategory)
    menureturn = input("Would you like to return to the Healthcare Helper? Y/N\n")
    if menureturn.lower() == "y":
        valid = True
        HCHelper()
    else:
        print("Goodbye!")
        exit()
def SC():
    steps = int(input("Enter step amount: "))
    totalkm = round(steps/1300,2)
    print(f"Your total km: {totalkm}")
    menureturn = input("Would you like to return to the Healthcare Helper? Y/N\n")
    if menureturn.lower() == "y":
        HCHelper()
        valid = True
    else:
        print("Goodbye!")
        exit()
def CBC():
    calories = int(input("Enter your calories: "))
    cpm = calories//60
    workouttime = int(input("Enter your workout time in minutes: "))
    calburnt = cpm*workouttime
    print(f"You've burnt: {calburnt} calories so far.")
    menureturn = input("Would you like to return to the Healthcare Helper? Y/N\n")
    if menureturn.lower() == "y":
        valid = True
        HCHelper()
    else:
        print("Goodbye!")
        exit()
def RR():
    heartrate = int(input("Enter your current heart rate: "))
    recoverytime = heartrate * (0.09**5)
    print(f"Recovery overtime: {recoverytime}")
    menureturn = input("Would you like to return to the Healthcare Helper? Y/N\n")
    if menureturn.lower() == "y":
        HCHelper()
        valid = True
    else:
        print("Goodbye!")
        exit()
def HCHelper():
    valid = True
    while valid:
        try:
            print("[bold red]Healthcare Helper Calculator[/bold red]")
            uchoice = int(input("Enter the corresponding number to the option you'd like:\n[1] Daily Dosage Calculator\n[2] BMI Calculator\n[3] Step Converter\n[4] Calories Burnt Calculator\n[5] Recovery Rate\n[6] Exit\n> "))
            if uchoice == 1:
                DDC()
                valid = False
            elif uchoice == 2:
                BMICALC()
                valid = False
            elif uchoice == 3:
                SC()
                valid = False
            elif uchoice == 4:
                CBC()
                valid = False
            elif uchoice == 5:
                RR()
                valid = False
            elif uchoice == 6:
                print("Goodbye!")
                valid = False
                exit()
            else:
                print("Incorrect value. Please re-enter")
                HCHelper() 
        except ValueError:
            print("Incorrect value. Please re-enter")
            HCHelper()
HCHelper()