from time import sleep
def rectanglearea1(): # Area of a rectangle calculator (cm)
    height = int(input("Enter the height (cm): "))
    length = int(input("Enter the length (cm): "))
    print("rectangle area is", height*length, "cm^2")

def timeconverter2(): # Minutes to Hours and Minutes converter
    minutes = int(input("Enter the amount of minutes: "))
    hours = minutes//60
    remainder = minutes%60
    print(hours,"hours", remainder, "minutes")

def billingsystem3(): # VAT Calculator
    costamount = float(input("Enter cost amount: "))
    vatcost = costamount/0.2
    print("Your cost with VAT applied is: ",vatcost)

def hospitalproject4(): # Patient Logger, VAT Calculator + Payment Plan Options. Includes an indented function
    name = input("Enter Patient Name: ")
    age = int(input("Enter Patient Age: "))
    billamount = float(input("Enter Bill Amount: "))
    billvat = round(billamount*1.2,2) # VAT Calculation
    if age < 18:
        discount = True
        if discount == True:
            discountvat = billvat/1.3 # Discount with VAT
        print("You have been applied a discount")
        print(f"Name: {name}\nAge: {age}\nBill, Discounted(VAT)£{discountvat}\nDiscount: Applied")
    else:
        print(f"Name: {name}\nAge: {age}\nBill (VAT): £{billvat}\nDiscount: N/A")
    def paymentoptions(): # Function for if their bill is > 1000
        if billvat > 1000:
            paymentplanoptions = int(input("Enter your payment plan number:\n1. Monthly Pay\n2. Full Pay\n"))
            if paymentplanoptions == 1 or paymentplanoptions == 2:
                print("Payment Plan Logged")
            else:
                print("Invalid, please reenter")
                paymentoptions()
        else:
            print("Good to go!")
    paymentoptions() # Prints the function if bill > 1000

def passwordchecker5(): # Password Checker using a while True loop
    validation = True
    password = input("Enter your password: ")
    while validation:
            correctpassword = password
            passwordinputter = input("Please enter your password: ")
            if passwordinputter != correctpassword:
                print("Invalid password, please reenter")
            else:
                print("Valid password!")
                validation = False
                exit()

def patientmenusystem6(): # How a menu system would work. Not fully functional
    valid = True
    print("Welcome to the Patient Menu!")
    while valid:
        optionpicker = int(input("What would you like to do?\n[1] Enter Patient Details\n[2] Calculate your BMI\n[3] Check your medicine dosage\n[4] Exit\n "))
        if optionpicker == 1:
            print("Taking you to the details prompt...")
            sleep(5)
            valid = False
        elif optionpicker == 2:
            print("Taking you to the BMI Calculator...")
            sleep(5)
            valid = False
        elif optionpicker == 3:
            print("Taking you to the medicine dosage logger...")
            sleep(5)
            valid = False
        elif optionpicker == 4:
            print("Exiting...")
            sleep(3)
            valid = False
            exit()
        else:
            print("Invalid Choice, please re-enter!\n\n")
