from time import sleep
def EHR():
    data = True
    while data:
        patientName = input("Enter your full name: ")
        patientAge = int(input("Enter your age: "))
        patientDate = input("Enter your Date of Birth (DD/MM/YY): ")
        patientHeight = int(input("Enter your height (cm): "))
        patientDetails = [patientName, patientAge, patientDate, patientHeight]
        print(patientDetails)
        sleep(2)
        confirmation = input(f"These are the details you inputted: \n {patientDetails} \n Are these correct? Y/N \n")
        if confirmation == "Y" or confirmation == "y":
            print(f"Confirmed Patient details: \n {patientDetails}")
            data = False
        else:
            print("Please reeenter your details:")
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
def MDT():
    MAXDOSAGE = int(input("Enter your max dosage: "))
    dosage1 = int(input("Enter your first dosage amount: "))
    dosage2 = int(input("Enter your second dosage amount: "))
    dosage3 = int(input("Enter your final dosage amount: "))
    dosagetotal = dosage1+dosage2+dosage3
    infoconfirmation = str(input("Are these the correct details? Y/N \n"))
    if infoconfirmation.lower() == "y":
        if dosagetotal > MAXDOSAGE:
            print(dosagetotal,"mg")
            print("Maximum amount: Exceeded")
            exit()
        else:
            print(dosagetotal, "mg")
            print("Maximum amount: Safe")
            exit()
    else:
        print("Please reenter")
        MDT()
def HBS():
    room = input("Did you purchase a room? Y/N ")
    if room.lower() == "y":
        roomcost = 100
    else:
        print("ok")
        roomcost = 1
    treatment = input("Did you receive a treatment? Y/N ")
    if treatment.lower() == "y":
        treatmentcost = 250
    else:
        print("ok")
        treatmentcost = 1
    docconsultation = input("Did you get doctor's consultation? Y/N ")
    if docconsultation.lower() == "y":
        docconsultation = 50
    else:
        print("ok")
        docconsultation = 1
    totalcost = roomcost + treatmentcost + docconsultation
    days = int(input("How many days have you spent here?: "))
    totalcostanddays = totalcost*(days/2)
    finaltotalcost = round(totalcostanddays//0.2,1)
    print("Your final cost comes to:£",finaltotalcost)

def menu():
    print("Function Menu:\nStoring Patient Data (EHR)\nBMI Calculator(BMICALC)\nMaximum Dosage Tracking(MDT)\nBill Calculator(HBS)")
    choice = str(input("Please input the Function you would like to access: "))
    if choice.lower() == "EHR":
        EHR()
    elif choice.lower() == "BMICALC":
        BMICALC()
    elif choice.lower() == "MDT":
        MDT()
    elif choice.lower() == "HBS":
        HBS()
    else:
        print("Invalid Choice")
        menu()
menu()

