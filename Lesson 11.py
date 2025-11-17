def medsafety():
    ageconfirm = int(input("Enter your age: "))
    weightconfirm = int(input("Enter your weight (kg): "))
    if ageconfirm > 12 and weightconfirm > 40:
        print("Safe to Give")
    else:
        print("Not safe")

def fitnesscentreaccess():
    medclearance = False
    ageconfirm = int(input("Enter your age: "))
    medclearanceconfirm = input("Do you have Medical Clearance? Y/N: ")
    if medclearanceconfirm.lower() == "y":
        medclearance = True
    if ageconfirm > 18 or medclearance == True:
            print("Access Granted")
    else:
        print("Access Denied")

def sleeptracker():
     notsleeping = True
     heartrate = int(input("Enter current heartrate: "))
     sleepconfirmation = input("Are you sleeping? Y/N: ")
     if sleepconfirmation.lower() == "y":
          notsleeping = False
     if notsleeping == True and heartrate > 100:
          print("Go to sleep!")
     else:
          print("No alert required")

def menu():
     val = True
     while val:
          try:
               print("--------MENU--------")
               uchoice = int(input("Enter the corresponding number to the function you'd like to access:\n[1] Medicine Safety Rule\n[2] Fitness Centre Access\n[3] Sleep Tracker Alert\n[4] Exit\n> "))
               if uchoice == 1:
                    medsafety()
                    val = False
               elif uchoice == 2:
                    fitnesscentreaccess()
                    val = False
               elif uchoice == 3:
                    sleeptracker()
                    val = False
               elif uchoice == 4:
                    print("Goodbye!")
                    val = False
               else:
                    print("Incorrect Value")
                    menu()
          except ValueError():
               print("Incorrect Value")
               menu()
menu()