calories = 0
workouttime = 0
steps = 0
valid = True
def calorieburn():
    calories = int(input("Enter your calories: "))
    cpm = calories//60
    workouttime = int(input("Enter your workout time in minutes: "))
    calburnt = cpm*workouttime
    print(f"You've burnt: {calburnt} calories so far.")
def stepconverter():
    steps = int(input("Enter step amount: "))
    totalkm = round(steps/1300,2)
    print(f"Your total km: {totalkm}")
def timecalculator():
    minutes = int(input("Enter the amount of minutes: "))
    hours = minutes//60
    remainder = minutes%60
    print(f"Time until next medication: {hours} hour(s) {remainder} minute(s)")
def medpackusage():
    tabletamount = int(input("How many tablets do you have?: "))
    peopleamount = int(input("How many people are you giving out to?: "))
    leftovertablets = tabletamount%peopleamount
    print(f"You have: {leftovertablets} tablet(s) left.")
def heartrecovery():
    heartrate = int(input("Enter your current heart rate: "))
    recoverytime = heartrate * (0.09**5)
    print(f"Recovery overtime: {recoverytime}")
    valid = True
while valid:
    try:
        uchoice = int(input("Welcome to the Fitness Tracker Menu. Select what you'd like to use:\n[1] Calorie Burn Calculator\n[2] Steps Conversion\n[3] Medication Timing\n[4] Tablet Distribution Remainder\n[5] Heart Recovery\n[6] Exit\n"))
        if uchoice == 1:
            calorieburn()
            valid = False
        elif uchoice == 2:
            stepconverter()
            valid = False
        elif uchoice == 3:
            timecalculator()
            valid = False
        elif uchoice == 4:
            medpackusage()
            valid = False
        elif uchoice == 5:
            heartrecovery()
            valid = False
        elif uchoice == 6:
            print("Goodbye!")
            valid = False
        else:
            print("Incorrect Value, please re-enter")
    except ValueError:
        print("Incorrect Value, please re-enter")
