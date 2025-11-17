from time import sleep
def steps():
    steps = 7345
    GOAL = 10000
    percentofgoal = round((steps/GOAL*100),0)
    remainingsteps = 10000-7345
    print(f"Goal Percentage: {percentofgoal}%")
    print(f"Steps Remaining: {remainingsteps}")



def BMIBuckets():
    weight = int(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))
    bmi = weight/(height**2)
    if bmi <= 18.5:
        print("Underweight")
    elif bmi <= 25:
        print("Healthy")
    elif bmi <= 30:
        print("Overweight")
    else:
        print("Obese")



def booleanlogic():
    dailyscreenminutes = int(input("Enter your daily screen time (minutes): "))
    steps = int(input("Enter your steps: "))
    nightscreenminutes = int(input("Enter your nightly screentime (minutes): "))
    def flag_user(dailyscreenminutes, steps, nightscreenminutes):
        if dailyscreenminutes > 240 and steps < 5000 or nightscreenminutes > 60:
            print(f"Flagged: {True}")
        else:
            print(f"Flagged: {False}")
    flag_user(dailyscreenminutes,steps,nightscreenminutes)



def hydration_streak():
    waterml = int(input("Enter your water intake (ml): "))
    regpoints = waterml//250
    if waterml >= 2000:
         bonuspoints = (waterml//2000)*5
         bonuspoints_regpoints = bonuspoints+regpoints
         print(f"Total Points: {bonuspoints_regpoints}")
    else:
         print(f"Total Points: {regpoints}")


def eligbility():
    age = int(input("Enter your age: "))
    lowincomeconfirmation = input("Are you a registered low-income participant? Y/N: ")
    monthfreeclass = input("Have you received a free class within the past: 30 days? Y/N: ")
    def eligibleforfreeclass(age, lowincomeconfirmation, monthfreeclass):
        if (age >= 16 and age <= 25 or lowincomeconfirmation.lower() == "y") and not monthfreeclass.lower() == "y":
            print(f"Eligible: {True}")
        else:
            print(f"Eligible: {False}")
    eligibleforfreeclass(age, lowincomeconfirmation, monthfreeclass)


def tiering():
    steps = int(input("Enter your weekly step count: "))
    water = int(input("Enter your weekly water intake (ml): "))
    points = (steps//1000)*2 + (water//500)
    def weekly_tier(steps,water):
        if points >= 0 and points <= 19:
            print(f"Total points: {points}")
            sleep(3)
            print("Bronze Tier")
        elif points >= 20 and points <= 39:
            print(f"Total points: {points}")
            sleep(3)
            print("Silver Tier")
        elif points >= 40:
            print(f"Total points: {points}")
            sleep(3)
            print("Gold Tier")
        else:
            print(f"Total points: {points}")
            sleep(3)
            print("Tierless")
    weekly_tier(steps,water)

def safedivandrounding():
    sessions = int(input("How many sessions?: "))
    totalmins = int(input("Total minutes: "))
    if sessions == 0:
        print("0")
    else:
        average = totalmins/sessions
        print(f"Average minutes per session: {round(average,1)}")


def dailysummary():
    GOAL = 10000
    steps = int(input("Steps: "))
    percentofgoal = round((steps/GOAL*100),0)
    water = int(input("Water intake (ml): "))
    regpoints = water//250
    screenmins = int(input("Screentime (m): "))
    if water >= 2000:
         bonuspoints = (water//2000)*5
         bonuspoints_regpoints = bonuspoints+regpoints
         if screenmins <= 240:
             print(f"Steps: {steps} ({percentofgoal}%)\nWater: {water} ml (+{bonuspoints_regpoints}pts)\nScreentime: {screenmins} -- OK")
         else:
             print(f"Steps: {steps} ({percentofgoal}%)\nWater: {water} ml (+{bonuspoints_regpoints}pts)\nScreentime: {screenmins} -- HIGH")
    else:
        if screenmins <= 240:
            print(f"Steps: {steps} ({percentofgoal}%)\nWater: {water} ml (+{regpoints}pts)\nScreentime: {screenmins} -- OK")
        else:
            print(f"Steps: {steps} ({percentofgoal}%)\nWater: {water} ml (+{regpoints}pts)\nScreentime: {screenmins} -- HIGH")

